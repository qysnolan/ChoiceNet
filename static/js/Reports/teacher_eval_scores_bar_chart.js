function barChartTeacherScore(container, account_type, dataset_teacher_scores,
                              teacher_average_score, title, yaxis_label,
                              chart_width, score_bar_color){
    
    var length = dataset_teacher_scores.length;
    var margin = {top: 35, right: 20, bottom: 35, left: 40},
    	width = chart_width - margin.left - margin.right,
    	height = chart_width - margin.top - margin.bottom - 5,
	    scaleXrange_self = 0.40;

	var color = d3.scale.ordinal()
        .domain([6,5,4,3,2,1])
        .range(score_bar_color);

	var x = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1);

	var y = d3.scale.linear()
        .range([height, margin.top*0.4]);

	var xAxis = d3.svg.axis()
	    			  .scale(x)
	    			  .orient("bottom");

    var formatAsPercentage = d3.format("%");

    var yAxis = d3.svg.axis()
	    			  .scale(y)
	    			  .orient("left")
                      .ticks(10)
                      .tickFormat(formatAsPercentage);

	var svg = d3.select(container)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");

	var max_Y = 1.00 ;

	x.domain(dataset_teacher_scores.map(function(d) { return d[0]; }));
	y.domain([0, max_Y]);

    var average_score = y(teacher_average_score);

    var line = d3.svg.line()
        .x(function(d,i) {
            if (i==0){ return 0 ;} return (x(d[0])+ x.rangeBand()); })
        .y(average_score);


	if(account_type==1) {
        svg.selectAll(".bar")
            .data(dataset_teacher_scores)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .on("click", function(d) {
                var url = "/viewReport/"+ d[2]+"/";
                $(location).attr('href',url);
            })
            .style("cursor", "pointer")
            .style("fill", function(d){
                if(d[1]>=0.9){ return color(1);}
                else if (d[1]>=0.8) {return color(2);}
                else if (d[1]>=0.7) {return color(3);}
                else if (d[1]>=0.6) {return color(4);}
                else if (d[1]>=0.5) {return color(5);}
                else {return color(6);}
            })
            .attr("x", function(d) {
                return x(d[0])+(x.rangeBand()*((1-scaleXrange_self)/2));
            })
            .attr("width", x.rangeBand()*scaleXrange_self)
            .attr("y", height)
            .attr("height",  0)
            .style("opacity", "0.0")
            .transition()
            .attr("y", function(d) {return y(d[1]); })
            .attr("height", function(d) { return (height - y(d[1])); })
            .style("opacity", "0.99")
            .duration(function(d) {
                return 200+(d[1] * 750 /d3.max(dataset_teacher_scores,
                    function(d) { return d[1];
                    }));
            })
            .delay(function(d,i){return (750 + i*150); });
    }
	
	//Create labels
	svg.selectAll(".mark")
	    .data(dataset_teacher_scores)
	    .enter()
	    .append("text")
	    .attr("class", "mark")
	    .text(function(d){return d[1]*100;})
	    .attr("x", function(d) {
            return x(d[0])+(x.rangeBand()/2)-x.rangeBand()/12;
        })
	    .attr("y", function(d) {
            return y(d[1])+x.rangeBand()/6;
        })
	    .attr("font-family", "sans-serif")
	    .attr("font-size", x.rangeBand()/6 + "px")
	    .attr("fill","white")
	    .style("opacity", "0.0")
	    .transition()
	    .style("opacity", "0.99")
	    .duration(function(d) {
            return 200+(d[1] * 750 /d3.max(dataset_teacher_scores,
                function(d) { return d[1]; }));
        })
	    .delay(function(d,i){return(1100 + i*150); });
	
	//Create average line	
	svg.append("path")
	   .datum(dataset_teacher_scores)
	   .attr("class", "line-bar")
	   .attr("d", line)
	   .style("opacity", "0.0")
	   .transition()
	   .style("opacity","0.99")
	   .duration(1000)
	   .delay(1500+length*150 );	
	
	//Create X axis
	svg.append("g")
	   .attr("class", "axis")
	   .attr("transform", "translate(0," + height + ")")
	   .call(xAxis)
	   .selectAll("text")
	   .style("text-anchor", "end")
	   .data(dataset_teacher_scores)
	   .attr("dx", "1.5em")
	   .attr("dy", ".8em")
	   .attr("transform", function(d) {
            return "translate(20,0)  rotate(-20)"
        })
	   .style("opacity", "0.0")
	   .text(function(d){ var date = d[0].split(" "); return date[0]})
	   .transition()
	   .style("opacity", "1.0")
	   .delay(function(d,i) {return (750 + i*150); })
	   .duration(function(d) {
            return 100+(d[1] * 750 /d3.max(dataset_teacher_scores,
                function(d) { return d[1]; }));
        });
	
	//Create Y axis
	var ty= svg.append("g")
	   .attr("class", "y axis")
	   .call(yAxis);
	
	ty.append("text")
	   .attr("transform", "rotate(-90)")
	   .attr("y", 3)
	   .attr("dy", ".71em")
	   .style("text-anchor", "end")
	   .text(yaxis_label);
	
	//Create Title
	svg.append("text")
	   .attr("x", (width / 2))
	   .attr("y", 0)
	   .attr("text-anchor", "middle")
	   .style("font-size", "16px")
	   .text(title);
	  
	}//end of the function