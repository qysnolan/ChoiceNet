/*  
  Uses the given container to draw a pie chart with the given data set.
  The pie chart is different depends on the user is teacher or not.
*/
function pieChart(container, dataset_piechart, account_type, title,
                  chart_width, pie_color_short, pie_color_long) {

	//Set svg attribute
    var width = chart_width,
	    height = chart_width - 5,
	    radius = Math.min(width, height) / 3,
	    padding = 60,
        color;
	
    //Adjust data for teacher user
	if (account_type == 0){
		color = d3.scale.ordinal()
                        .range(pie_color_long);
	}
	else {
		color = d3.scale.ordinal()
	    			    .range(pie_color_short);
	}
	
	var arc_before = d3.svg.arc()
	    				   .outerRadius(radius - radius*0.618)
	    				   .innerRadius(radius - radius*0.618);
	    			
	var arc_after = d3.svg.arc()
	    				  .outerRadius(radius - 10)
	    				  .innerRadius(radius - radius*0.618);
	
	var pie = d3.layout.pie()
	    			   .sort(null)
	    			   .value(function(d) { return d[1]; });

    //Append svg
	var svg_pie = d3.select(container)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" +(width / 2 - padding +20)
            + "," + height / 2 + ")");

	var g = svg_pie.selectAll(".arc")
                   .data(pie(dataset_piechart))
                   .enter()
                   .append("g")
                   .attr("class", "arc");

    //Append pie graph
    g.append("path")
        .attr("d", arc_before)
        .style("fill", "#fffdf6")
        .transition()
        .attr("d", arc_after)
        .style("fill", function(d) { return color(d.data[0]); })
        .duration(1500)
        .delay(500);

    g.append("text")
        .attr("transform", function(d) { return "translate(" +
             arc_after.centroid(d) + ")"; })
        .attr("dy", ".35em")
        .style("text-anchor", "middle")
        .text(function(d) {
             if (d.data[1]!=0){
                 return d.data[1];
             }
             else {
                 return null;
             }
         })
        .attr("fill", "#fffdf6")
        .transition()
        .attr("fill", "black")
        .duration(1000)
        .delay(1200);

	//Create Title   
	svg_pie.append("text")
		   .attr("font-size", "16px")
           .attr("x", padding/2+10)
           .attr("y", -(height/2)+(padding/2)+15)
           .attr("text-anchor", "middle")
           .text(title);
	 
	//Create Legend  
	var legend = svg_pie.selectAll(".legend")
        .data(color.domain().slice().reverse())
        .enter().append("g")
        .attr("class", "legend")
        .attr("transform", function(d, i) {
            return "translate(0," + i * 20 + ")";
        });

	legend.append("rect")
          .attr("x", width/2+5)
          .attr("y", width * 0.07)
          .attr("width", 0)
          .attr("height", 18)
          .style("fill", color)
          .transition()
          .duration(1500)
          .delay(500)
          .attr("width", 18)
          .style("stroke","gray" )
          .style("stroke-width","0.3");

    //Adjust legend for teacher user
    var legend_num = 9;
    legend.append("text")
        .attr("x", width/2+3)
        .attr("y", width * 0.07 + 10)
        .style("text-anchor", "end")
        .text(function(d) {
            if (account_type == 0){
                if (legend_num<5) {
                    return "0-49%";}
                else if (legend_num == 9){
                    legend_num--;
                    return "90-100%";
                }
                else {
                    var temp = legend_num;
                    legend_num--;
                    return temp+"0-"+((temp+1)*10-1)+"%";
                }
            }
            else {
                if (legend_num == 9){
                    legend_num--;
                    return "Examplary";
                }
                else if (legend_num == 8){
                    legend_num--;
                    return "Profient";
                }
                else if (legend_num == 7){
                    legend_num--;
                    return "Needs Improvement";
                }
                else {
                    legend_num--;
                    return "Unsatifactory";
                }
            }
            }
        );
} // end pieChart funciton
