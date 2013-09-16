/*
  Uses the given container to draw a line chart with the given data set.
  User can click the bar to get the view evaluation page.
*/
function evalScoreSelf(container, account_type, dataset_teacher_scores,
                              teacher_average_score, title, yaxis_label,
                              chart_width, score_bar_color){

    //Set svg attribute
    var length = dataset_teacher_scores.length;
    var margin = {top: 50, right: 30, bottom: 50, left: 60},
    	width = chart_width - margin.left - margin.right,
    	height = (chart_width/3) - margin.top - margin.bottom - 5,
	    scaleXrange_self = 0.40;

    //Set color set
	var color = d3.scale.ordinal()
        .domain([6,5,4,3,2,1])
        .range(score_bar_color);

    // Set x and y axis
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

    //Append svg
	var svg_score_self = d3.select(container)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");

	var max_Y = 1.00 ;

    //Set domain
	x.domain(dataset_teacher_scores.map(function(d) { return d[0]; }));
	y.domain([0, max_Y]);

    var average_score = y(teacher_average_score);

    var line = d3.svg.line()
        .x(function(d,i) {
            if (i==0){ return 0 ;} return (x(d[0])+ x.rangeBand()); })
        .y(average_score);

    //Append bars
	if(account_type==1) {
        svg_score_self.selectAll(".bar")
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
                if (x.rangeBand()*scaleXrange_self<(chart_width/20)){
                    return x(d[0])+(x.rangeBand()*((1-scaleXrange_self)/2));
                }
                else if (x.rangeBand()*scaleXrange_self<(chart_width/5)){
                    return x(d[0])+(x.rangeBand()*((1-scaleXrange_self/2)/2));
                }
                else {
                    return x(d[0])+(x.rangeBand()*((1-scaleXrange_self/4)/2));
                }
            })
            .attr("width", function(d){
                if (x.rangeBand()*scaleXrange_self<(chart_width/20)){
                    return x.rangeBand()*scaleXrange_self;
                }
                else if (x.rangeBand()*scaleXrange_self<(chart_width/5)){
                    return x.rangeBand()*(scaleXrange_self/2);
                }
                else {
                    return x.rangeBand()*(scaleXrange_self/4);
                }
            })
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
	svg_score_self.selectAll(".mark")
	    .data(dataset_teacher_scores)
	    .enter()
	    .append("text")
	    .attr("class", "mark")
	    .text(function(d){return d[1]*100;})
	    .attr("x", function(d) {
            if (x.rangeBand()*scaleXrange_self<(chart_width/20)){
                return x(d[0])+(x.rangeBand()/2)-x.rangeBand()/12;
            }
            else if (x.rangeBand()*scaleXrange_self<(chart_width/5)){
                return x(d[0])+(x.rangeBand()/2)-x.rangeBand()/24;
            }
            else {
                return x(d[0])+(x.rangeBand()/2)-x.rangeBand()/48;
            }
        })
	    .attr("y", function(d) {
            if (x.rangeBand()*scaleXrange_self<(chart_width/20)){
                return y(d[1])+x.rangeBand()/6;
            }
            else if (x.rangeBand()*scaleXrange_self<(chart_width/5)){
                return y(d[1])+x.rangeBand()/12;
            }
            else {
                return y(d[1])+x.rangeBand()/24;
            }
        })
	    .attr("font-family", "sans-serif")
	    .attr("font-size", function(d) {
            if (x.rangeBand()*scaleXrange_self<(chart_width/20)){
                return x.rangeBand()/6 + "px";
            }
            else if (x.rangeBand()*scaleXrange_self<(chart_width/5)){
                return x.rangeBand()/12 + "px";
            }
            else {
                return x.rangeBand()/24 + "px";
            }
        })
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
	svg_score_self.append("path")
	   .datum(dataset_teacher_scores)
	   .attr("class", "line-bar")
	   .attr("d", line)
	   .style("opacity", "0.0")
	   .transition()
	   .style("opacity","0.99")
	   .duration(1000)
	   .delay(1500+length*150 );
    //Create average label
    svg_score_self.append("text")
        .attr("x", width)
	    .attr("y", average_score*0.95)
        .attr("class", "axis")
        .style("opacity", "0.0")
	    .attr("text-anchor", "end")
        .text("Average")
        .transition()
	    .style("opacity","0.99")
        .duration(1000)
	    .delay(1500+length*150 );
	
	//Create X axis
    //For IE 8 rotate issue
    if (isIE()!=false && isIE() < 9){
        svg_score_self.append("g")
           .attr("class", "axis")
           .attr("transform", "translate(0," + height + ")")
           .call(xAxis)
           .selectAll("text")
           .style("text-anchor", "end")
           .data(dataset_teacher_scores)
           .attr("transform", function(d) {
                return "translate(50,-10) rotate(-35)"
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
    }
    else{
        svg_score_self.append("g")
           .attr("class", "axis")
           .attr("transform", "translate(0," + height + ")")
           .call(xAxis)
           .selectAll("text")
           .style("text-anchor", "end")
           .data(dataset_teacher_scores)
           .attr("transform", function(d) {
                return "rotate(-45)"
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
    }
	
	//Create Y axis and label
	var ty= svg_score_self.append("g")
	   .attr("class", "y axis")
	   .call(yAxis);
	
	ty.append("text")
	   .attr("transform", "rotate(-90)")
	   .attr("y", 10)
	   .attr("x", -10)
	   .style("text-anchor", "end")
	   .text(yaxis_label);
	
	//Create Title
	svg_score_self.append("text")
	   .attr("x", (width / 2))
	   .attr("y", -10)
	   .attr("text-anchor", "middle")
	   .style("font-size", "16px")
	   .text(title);

    //get IE version
    function isIE () {
        var myNav = navigator.userAgent.toLowerCase();
        return (myNav.indexOf('msie') != -1) ?
            parseInt(myNav.split('msie')[1]) : false;
    }
	  
	}//end of the function