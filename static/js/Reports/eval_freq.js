/*
  Uses the given container to draw a line chart with the given data set.
  User can choose time length - three, six, twelve months and total.
*/
function evalFreq(container, control, dataset_line, account_type, title,
                  chart_width) {

    //Set svg attribute
    var margin = {top: 40, right: 60, bottom: 50, left: 60},
        width = chart_width - margin.left - margin.right,
        height = chart_width/3.3 - margin.top - margin.bottom - 30;

    //Set month array
    var monthNames = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec" ];
    var max_Y = 0;

    //Initializing data
    for (var k=0; k<dataset_line.length; k++){
        if (dataset_line[k].frequency.length > 0){
            // Find max value
            if (max_Y < d3.max(dataset_line[k].frequency,
                function(d) { return d.count; })){
                max_Y = d3.max(dataset_line[k].frequency,
                    function(d) { return d.count; });
            }
            // Set date format
            for (var i=0; i<dataset_line[k].frequency.length; i++){
                var date = dataset_line[k].frequency[i].date.split("-");
                date = monthNames[date[0]-1] + "-" + date[1];
                dataset_line[k].frequency[i].date = date;
            }
        }
        //Abbreviate name
        if (dataset_line[k].name.length > 15){
            dataset_line[k].name = dataset_line[k].name.substring(0,15) + ".";
        }
    }

    var color = d3.scale.category20();

    // Set x and y axis
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

    //Append svg
    var svg_line_freq = d3.select(container)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");

    //Set x axis value
    var three_months = [], six_months = [], one_year = [], total = [];
    var total_length;
    var pos = 0;
    // find the first none null frequency set
    for (var r=0; r<dataset_line.length; r++){
        if(dataset_line[r].frequency.length>0){
            pos = r;
            break;
        }
    }
    total_length = dataset_line[pos].frequency.length;
    for (var w=0; w<total_length; w++){
        total.push(dataset_line[pos].frequency[w].date);
        if (w>=total_length-13){
            one_year.push(dataset_line[pos].frequency[w].date);
        }
        if (w>=total_length-7){
            six_months.push(dataset_line[pos].frequency[w].date);
        }
        if (w>=total_length-4){
            three_months.push(dataset_line[pos].frequency[w].date);
        }
    }
    var x_axis = {
        "three-months": three_months,
        "six-months": six_months,
        "one-year": one_year,
        "total": total
    };

    //Show total as default
    var time = 7;
    redraw(time, six_months);

    //Change graph as user selected
    var menu = d3.select(control)
        .on("change", change);

    var time_length = {
        "three-months": 4,
        "six-months": 7,
        "one-year": 13,
        "total": dataset_line[pos].frequency.length
    };

    function change() {
        var series = menu.property("value");
        position = [];
        redraw(time_length[series], x_axis[series]);
    }

    //Draw function
    function redraw(time, x_label) {

        //Remove old graph
        svg_line_freq.selectAll("path").remove();
        svg_line_freq.selectAll("text").remove();
        svg_line_freq.select(".x.axis").remove();

        //Set start point
        var time_start = dataset_line[pos].frequency.length-time-1;

        //Set "d" attr
        var line_init = d3.svg.line()
            .interpolate("monotone")
            .x(function(d,i) {
                if (i>time_start){
                    return x(d.date) + x.rangeBand()/2;
                }
                else {
                    return null;
                }
            })
            .y(height);
        var line = d3.svg.line()
            .interpolate("monotone")
            .x(function(d,i) {
                if (i>time_start){
                    return x(d.date) + x.rangeBand()/2;
                }
                else {
                    return null;
                }
            })
            .y(function(d,i) {
                if (i>time_start){
                    return y(d.count);
                }
                else {
                    return height;
                }
            });

        //"Reset label" choice
        svg_line_freq.append("text")
            .attr("x", width-40)
            .attr("y", -15)
            .style("text-decoration","underline")
            .attr("class", "btn")
            .on("click", change)
            .text("Reset graph");

        //Set domain
        x.domain(x_label.map(function(d) {return d;}));
        y.domain([0,max_Y]);

        //Draw x and y axis
        //Solve IE 8 rotate problem
        if (isIE()!=false && isIE() < 9){
            svg_line_freq.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis)
                .selectAll("text")
                .attr("class","x text")
                .style("text-anchor", "middle");
        }
        else{
            svg_line_freq.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis)
                .selectAll("text")
                .attr("class","x text")
                .style("text-anchor", "end")
                .attr("transform", "rotate(-45)");
        }
        svg_line_freq.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0.3*margin.left)
            .style("text-anchor", "end");

        //Draw lines
        for (var l=0; l<dataset_line.length; l++){
            //only draw the user has evaluation
            if (dataset_line[l].frequency.length > 1){
                svg_line_freq.append("path")
                    .datum(dataset_line[l].frequency)
                    .attr("class", "line")
                    .attr("d", line_init)
                    .style("stroke", color(dataset_line[l].name))
                    .transition()
                    .duration(1000)
                    .attr("d", line);
            }
        }

        //Show teacher names
        for (l=0; l<dataset_line.length; l++){
            if (dataset_line[l].frequency.length > 1){

                //Find the right highest position
                var j = 0,
                    max = dataset_line[l].frequency[0].count,
                    max_index = 0;

                while(++j < dataset_line[l].frequency.length) {
                    if((dataset_line[l].frequency[j].count >= max)
                        && (dataset_line[l].frequency[j].count > 0)) {
                        max_index = j;
                        max = dataset_line[l].frequency[j].count;
                    }
                }
                // For IE 8 large number can cause error
                if (isIE()!=false && isIE() < 9){
                    if(y(dataset_line[l].frequency[max_index].count)<150
                        && max_index>time_start){
                        svg_line_freq.append("text")
                            .attr("transform", "translate("
                                + (x(dataset_line[l].frequency[max_index].
                                date)+x.rangeBand()/2)
                                + "," +
                                y(dataset_line[l].frequency[max_index].count)
                                + ") rotate(-45)")
                            .attr("class", "legend btn")
                            .attr("fill", color(dataset_line[l].name))
                            .on("click", moveLabel)
                            .text(dataset_line[l].name);
                    }
                }
                else{
                    if(max_index>time_start){
                        svg_line_freq.append("text")
                            .attr("transform", "translate("
                                + (x(dataset_line[l].frequency[max_index].
                                date)+x.rangeBand()/2) +
                                "," +
                                y(dataset_line[l].frequency[max_index].count)
                                + ") rotate(-45)")
                            .attr("class", "legend btn")
                            .attr("fill", color(dataset_line[l].name))
                            .on("click", moveLabel)
                            .text(dataset_line[l].name);
                    }
                }
            }
        }
    }//end redraw function

    //move label function
    var position = [];
    function moveLabel(){
        var label = d3.select(this);
        if(label.attr("transform").substring(0,14) == "translate(0,0)"){
            for(var v=0; v<position.length; v++){
                if(label.attr("y") == position[v].new_pos){
                    label.transition()
                        .duration(500)
                        .attr("x", 0)
                        .attr("y", 0)
                        .attr("transform", position[v].old_pos);
                    break;
                }
            }
        }
        else{
            var old_pos = label.attr("transform"), new_pos = 0;
            if (position.length == 0){
                new_pos =  0;
            }
            else{
                new_pos = position[position.length-1].new_pos + 12;
            }
            position.push({old_pos:old_pos,new_pos:new_pos});
            label.transition()
                .duration(500)
                .attr("x", width-40)
                .attr("y", new_pos)
                .attr("transform", "translate(0,0) rotate(0)");
        }
    }
    //get IE version
    function isIE () {
        var myNav = navigator.userAgent.toLowerCase();
        return (myNav.indexOf('msie') != -1) ?
            parseInt(myNav.split('msie')[1]) : false;
    }
}// end evalFreq function