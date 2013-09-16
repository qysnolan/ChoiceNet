/*  
  Uses the given container to draw a bar chart with the given data set.
  This bar chart also has sort option.
*/
function barChart(container, control, dataset_barchart, account_type, title,
                  xaxis_label, yaxis_label, chart_width, chart_width_long,
                  bar_color) {
	//Set svg attribute
    var margin = {top: 20, right: 20, bottom: 80, left: 60},
    	width = chart_width_long - margin.left - margin.right,
    	height = chart_width - margin.top - margin.bottom -30,
	    scaleXrange = 0.4;
	var color = d3.scale.ordinal()
        .range(bar_color);

    //Set x and y axis
	var x = d3.scale.ordinal()
	                .rangeRoundBands([0, width], .1);
	
	var y = d3.scale.linear()
	    			.range([height, margin.top*0.4]);
	
	var xAxis = d3.svg.axis()
	    			  .scale(x)
	    			  .orient("bottom");
	
	var yAxis = d3.svg.axis()
	    			  .scale(y)
	    			  .orient("left");

    //Draw svg
	var svg_bar = d3.select(container)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");


    //Find max value of y
	var max_Y = 0;
	if (account_type == 0) {
		max_Y = 100;
		} 
	else {
		max_Y = d3.max(dataset_barchart, function(d) { return d[1]+1; });
		}
			
	//Domain of x and y axis
    x.domain(dataset_barchart.map(function(d) { return d[0]; }));
	y.domain([0, max_Y]);
	
	//Transition time
	var duration_bar = function(d) {
        return 100+(d[1] * 750 /d3.max(dataset_barchart,
            function(d) {
                return d[1];
            }));
    };
	
	//Create bars
    if(account_type==1) {
        svg_bar.selectAll(".bar")
            .data(dataset_barchart)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .style("fill", function(d) { return color(d[1]); })
            .attr("x", function(d) {
                return x(d[0])+(x.rangeBand()*((1-scaleXrange)/2));
            })
            .attr("width", x.rangeBand()*scaleXrange)
            .attr("y", height)
            .attr("height",  0)
            .transition()
            .attr("height", function(d) { return (height - y(d[1])); })
            .attr("y", function(d) { return y(d[1]);})
            .duration(duration_bar)
            .delay(750)
            .style("stroke","gray" )
            .style("stroke-width","0.3");
	   }
    else{
        svg_bar.selectAll(".bar")
            .data(dataset_barchart)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .attr("x", function(d) {
                return x(d[0])+(x.rangeBand()*((1-scaleXrange)/2));
            })
            .attr("width", x.rangeBand()*scaleXrange)
            .attr("y", height)
            .attr("height", 0)
            .transition()
            .attr("height", function(d) { return (height - y(d[1])); })
            .attr("y", function(d) { return y(d[1]); })
            .duration(duration_bar)
            .delay(750)
            .style("stroke","gray" )
            .style("stroke-width","0.3");
    }
	
	//Create X axis
    //IE 8 rotate issue
    if (isIE()!=false && isIE() < 9){
        svg_bar.append("g")
               .attr("class", "x axis")
               .attr("transform", "translate(0," + height + ")")
               .call(xAxis)
               .selectAll("text")
               .attr("class","x text")
               .style("text-anchor", "end")
               .style("opacity", "0.0")
               .attr("transform", "translate(50,-10) rotate(-35)");
    }
    else{
        svg_bar.append("g")
               .attr("class", "x axis")
               .attr("transform", "translate(0," + height + ")")
               .call(xAxis)
               .selectAll("text")
               .attr("class","x text")
               .style("text-anchor", "end")
               .style("opacity", "0.0")
               .attr("transform", "rotate(-45)");
    }
	
	//Create Y axis   
	svg_bar.append("g")
           .attr("class", "y axis")
           .call(yAxis)
           .append("text")
           .attr("transform", "rotate(-90)")
           .attr("y", 10)
           .style("text-anchor", "end")
           .text(yaxis_label);
	   
	//Create Title   
	svg_bar.append("text")
	       .attr("font-size", "16px")
           .attr("x", (width / 2))
           .attr("y", 0)
           .attr("text-anchor", "middle")

           .text(title);
           
    //Sort Value
    d3.select(control).on("click", change);

    var sortTimeout = setTimeout(function() {
            d3.select(control).property("checked", false).each(change);
        }, 2000
    );

    //Sort function
    function change() {
        clearTimeout(sortTimeout);

        // Copy-on-write since tweens are evaluated after a delay.
        var x0 = x.domain(dataset_barchart.sort(this.checked
          ? function(a, b) { return b[1] - a[1]; }
          : function(a, b) { return d3.ascending(a[2], b[2]);})
          .map(function(d) { return d[0]; }))
          .copy();

        var transition = svg_bar.transition().duration(750),
          delay = function(d, i) { return i * 50; };

        transition.selectAll(".bar")
            .delay(delay)
            .attr("x", function(d) {
                return x0(d[0])+(x.rangeBand()*((1-scaleXrange)/2));
            });

        svg_bar.selectAll(".x.axis")
             .call(xAxis);
        //Solve IE 8 rotate issue
        if (isIE()!=false && isIE() < 9){
            svg_bar.selectAll(".x.axis")
                 .selectAll("text")
                 .style("text-anchor", "end")
                 .style("opacity", "0.0")
                 .transition()
                 .style("opacity", "0.99")
                 .duration(1000)
                 .delay(100)
                 .attr("transform", "translate(50,-10) rotate(-35)");
        }
        else{
            svg_bar.selectAll(".x.axis")
                 .selectAll("text")
                 .style("text-anchor", "end")
                 .style("opacity", "0.0")
                 .transition()
                 .style("opacity", "0.99")
                 .duration(1000)
                 .delay(100)
                 .attr("transform", "rotate(-45)");
        }
    }//end change function

    //Get IE version
    function isIE () {
        var myNav = navigator.userAgent.toLowerCase();
        return (myNav.indexOf('msie') != -1) ?
            parseInt(myNav.split('msie')[1]) : false;
    }

} // end barChart function
