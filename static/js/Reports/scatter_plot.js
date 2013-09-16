/*  
  Uses the given container to draw a scatter plot with the given data set.
  This graph can change between bar chart and scatter chart.
  Draws scatter plot for admin's dashboard.
*/
function scatterPlot(container, control, dataset_scatterplot, title,
                     xaxis_label, yaxis_label, chart_width, chart_width_medium,
                     scatter_color) {
 	//Set svg attribute
	var margin = {top: 20, right: 20, bottom: 20, left: 50};
	var width = chart_width_medium - margin.left - margin.right;
	var height = chart_width - margin.top - margin.bottom - 30;
	var scaleRange = 0.4;
    var radius;

	var color = d3.scale.ordinal()
            .range(scatter_color);
	
	// Set x and y axis and radius
	var xScale = d3.scale.linear()						 
			 			 .domain([40, 100])
			 			 .range([0, width-margin.right]);

	var yScale = d3.scale.linear()
            .domain([0, d3.max(dataset_scatterplot, function(d) {
                return d[1];
            })*1.2])
            .range([height, margin.top*1.8]);
	
	var rScale = d3.scale.linear()
            .domain([0, d3.max(dataset_scatterplot, function(d) {
                return d[1];
            })])
            .range([2, 5]);

	if (chart_width == chart_width_medium){
        radius = 0.05;
    }
    else {
        radius = 0.025;
    }
	//Define X axis
	var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom")
            .ticks(5)
            .tickFormat( function(d) {
                if (d<50) {return 0;} else {return d;}
            });
	
	//Define Y axis
	var yAxis = d3.svg.axis()
		  			  .scale(yScale)
		  			  .orient("left")
		  			  .ticks(5)
		  			  .tickFormat(d3.format("d"));
	
	//Create SVG element
	var svg_scatter = d3.select(container)
				        .append("svg")
				        .attr("width", width + margin.left + margin.right)
				        .attr("height", height + margin.top + margin.bottom)
				        .attr("transform", "translate(0 ," + margin.top + ")");
	
	//Transition time
	var duration_scatter = function(d) {
            return 100+(d[1] * 750 /d3.max(dataset_scatterplot,
                function(d) {
                    return d[1];
                }));
        };
	
	//Create bars   
	svg_scatter.selectAll(".bar")
        .data(dataset_scatterplot)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function(d) {
            return xScale(d[0]) + margin.left - (((width - margin.right) /
                dataset_scatterplot.length) * scaleRange)/2;
        })
        .attr("width", ((width - margin.right) / dataset_scatterplot.length) *
            scaleRange)
        .attr("y", height)
        .attr("height", 0)
        .transition()
        .attr("height", function(d) { return height - yScale(d[1]); })
        .attr("y", function(d) { return yScale(d[1]); })
        .duration(duration_scatter)
        .delay(750)
        .style("fill", function(d) { return color(d[0]); })
        .style("stroke","gray" )
        .style("stroke-width","0.3");
	   
	//Create scatter and disappear by default 
	svg_scatter.selectAll("circle")
        .data(dataset_scatterplot)
        .enter()
        .append("circle")
        .attr("cx", function(d) {
            return xScale(d[0])+margin.left;
        })
        .attr("cy", function(d) {
            return yScale(d[1]);
        })
        .attr("r", 0)
        .style("fill", function(d) { return color(d[0]); })
        .style("stroke","gray" )
        .style("stroke-width","0.3");
	
	//Create labels for scatter
	svg_scatter.selectAll("text")
        .data(dataset_scatterplot)
        .enter()
        .append("text")
        .attr("class","label_scatter")
        .text(function(d) { if (d[1]!=0) {return d[1];} else {return null;}
        })
        .attr("x", function(d) {
            return xScale(d[0])-3 + margin.left;
        })
        .attr("y", function(d) {
            return yScale(d[1])+3;
        })
        .attr("fill", "black");
	
	//scatter disappear by default   	
	svg_scatter.selectAll("text.label_scatter")
	           .style("opacity", "0.0");
	               
	//Create X axis
	svg_scatter.append("g")
        .attr("class", "axis")
        .attr("transform", "translate("+ margin.left +"," + height + ")")
        .call(xAxis)
        .append("text")
        .attr("x", width)// - margin.left*0.3)
        .attr("y", -6)
        .style("text-anchor", "end")
        .text(xaxis_label);

	//Create Y axis
	svg_scatter.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(" + margin.left + ",0)")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .style("text-anchor", "end")
        .attr("y", 10)
        .attr("x", -margin.top*1.8)
        .text(yaxis_label);
	   
	//Create Title   
	svg_scatter.append("text")
        .attr("font-size", "16px")
        .attr("x", (width + margin.left + margin.right)/2)
        .attr("y", margin.top)
        .attr("text-anchor", "middle")
        .text(title);

    //Scatter
    d3.select(control).
        on("click", change);

    //Scatter function
    function change() {

        var value = this.checked;

        if(value)  {
            svg_scatter.selectAll("rect")
                .transition()
                .attr("height", 0)
                .duration(duration_scatter)
                .delay(10);

            svg_scatter.selectAll("circle")
                .transition()
                .attr("r", function(d) {return rScale(d[1]*width*radius); })
                .duration(duration_scatter)
                .delay(10);

            svg_scatter.selectAll("text.label_scatter")
                .transition()
                .style("opacity", "0.99")
                .duration(10)
                .delay(200);
        }
        else{
            svg_scatter.selectAll("circle")
                .transition()
                .attr("r", "0")
                .duration(duration_scatter)
                .delay(10);

            svg_scatter.selectAll("text.label_scatter")
                .transition()
                .style("opacity", "0.0")
                .duration(10)
                .delay(200);

            svg_scatter.selectAll("rect")
                .transition()
                .attr("height", function(d) { return (height - yScale(d[1]));})
                .duration(duration_scatter)
                .delay(10);
        }
    }//end scatter change function
} // end scatterPlot function
