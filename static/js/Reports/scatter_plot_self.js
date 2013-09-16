/*  
  Uses the given container to draw a scatter plot with the given data set.
  This graph can change between bar chart and scatter chart.
  Draws scatter plot for teacher's dashboard.
*/
function scatterPlotSelf(container, dataset_scatterplot_self,
                         dataset_scatterplot_axis_self, title, chart_width) {
    //Set svg attribute
	var margin = {top: 30, right: 20, bottom: 30, left: 30},
    	width = chart_width - margin.left - margin.right,
    	height = chart_width - margin.top - margin.bottom - 5;

    // Set x and y axis
	var x = d3.scale.ordinal()
	                .rangeRoundBands([0, width], .1);
	
	var y = d3.scale.linear()
	    			.range([height-margin.bottom, margin.top]);
	
	var xAxis = d3.svg.axis()
	    			  .scale(x)
	    			  .orient("bottom");

    //Append svg
	var svg_scatter_self = d3.select(container)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");

    //Set domain
	x.domain(dataset_scatterplot_self.map(function(d) { return d[0]; }));
	y.domain([0, 100]);

    //Create scatters
	svg_scatter_self.selectAll("circle")
        .data(dataset_scatterplot_self)
        .enter()
        .append("circle")
        .attr("cx", function(d) { return x(d[0])+(x.rangeBand()*0.5); })
        .attr("cy", function(d) { return y(d[1]); })
        .attr("r", 0)
        .attr("fill","rgb(20,188,224)")
        .attr("height", function(d) { return height - y(d[1]); })
        .transition()
        .duration(1500)
        .delay(500)
        .attr("r", (chart_width/50))
        .style("stroke","gray" )
        .style("stroke-width",0.3);
	
	if (dataset_scatterplot_self.length != 0){              	
		//Create X axis
        //For IE 8 rotate issue
        if (isIE()!=false && isIE() < 9){
            svg_scatter_self.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + (height-margin.bottom) + ")")
                .call(xAxis)
                .selectAll("text")
                .style("text-anchor", "end")
                .attr("transform", "translate(50,-10) rotate(-35)");
        }
        else{
            svg_scatter_self.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + (height-margin.bottom) + ")")
                .call(xAxis)
                .selectAll("text")
                .style("text-anchor", "end")
                .attr("transform", "rotate(-45)");
        }
    }
    else{
    //If there is no data, show message
	    svg_scatter_self.append("text")
            .attr("class", "label_scatter")
            .attr("x", width/2)
            .attr("y", height/2)
            .attr("text-anchor", "middle")
            .text("No data for this period");
    }
              
	//Create Title   
 	svg_scatter_self.append("text")
                    .attr("x", width/2)
                    .attr("y", margin.top-15)
                    .attr("text-anchor", "middle")
                    .style("font-size", "16px")
                    .text(title);
	   
	//Append lines for reference
	var legend = svg_scatter_self.selectAll(".legend")
                                .data(dataset_scatterplot_axis_self)
                                .enter().append("g")
                                .attr("class", "legend")
                                .attr("y", function(d) { return y(d[0]); })
                                .attr("x",10);

    legend.append("line")
          .attr("y1", function(d) { return y(d[0]); })
          .attr("y2", function(d) { return y(d[0]); })
          .attr("x1",0)
      	  .attr("x2", width)
      	  .attr("stroke","gray")
      	  .attr("stroke-width","1");

    legend.append("text")
          .attr("y", function(d) { return y(d[0])-8; })
          .attr("x", -15)
          .attr("dy", ".35em")
          .text(function(d) { return d[1]; });

    //get IE version
    function isIE () {
        var myNav = navigator.userAgent.toLowerCase();
        return (myNav.indexOf('msie') != -1) ?
            parseInt(myNav.split('msie')[1]) : false;
    }

} // end scatterPlotSelf function
