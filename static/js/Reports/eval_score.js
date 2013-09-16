/*
  Uses the given container to draw a line chart with the given dataset.
  This line chart has time length.
*/
function evalScore(container, control, dataset_line, account_type, title,
                  chart_width) {

    //Set svg attribute
    var margin = {top: 40, right: 80, bottom: 60, left: 60},
        width = chart_width - margin.left - margin.right,
        height = chart_width/3.3 - margin.top - margin.bottom - 30;

    //Set date format
    var parseDate = d3.time.format("%b-%d-%Y").parse;
    //Set month array
    var monthNames = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec" ];
    var max_Y = 0;

    //Change date format and fill out null value
    for (var k=0; k<dataset_line.length; k++){
        if (dataset_line[k].frequency.length > 0){
            //find the largest y
            if (max_Y < d3.max(dataset_line[k].frequency,
                function(d) { return d.count; })){
                max_Y = d3.max(dataset_line[k].frequency,
                    function(d) { return d.count; });
            }
            //Set date format
            for (var i=0; i<dataset_line[k].frequency.length; i++){
                var date = new Date(Date.parse(
                    dataset_line[k].frequency[i].date
                ));
                date = monthNames[date.getMonth()] + "-" + date.getDate() + "-"
                    + date.getFullYear();
                dataset_line[k].frequency[i].date = parseDate(date);
            }
            //fill out null value
            for (var h=0; h<dataset_line[k].frequency.length; h++){
                if (dataset_line[k].frequency[h].count != 0){
                    var date_before = new Date(),
                        date_after = new Date();
                    var temp_date = dataset_line[k].frequency[h].date;
                    date_before.setTime(temp_date.getTime()-1000*60*60*24);
                    date_after.setTime(temp_date.getTime()+1000*60*60*24);
                    if (h>0 && dataset_line[k].frequency[h-1].date.getTime()!=
                        date_before.getTime()){
                        dataset_line[k].frequency.push({
                            date:date_before,count:0
                        });
                    }
                    else if (h==0){
                        dataset_line[k].frequency.push({
                            date:date_before,count:0
                        });
                    }
                    if (h == dataset_line[k].frequency.length-1){
                        dataset_line[k].frequency.push({
                            date:date_after,count:0
                        });
                    }
                    else if (dataset_line[k].frequency[h+1].date.getTime()!=
                        date_after.getTime()){
                        dataset_line[k].frequency.push({
                            date:date_after,count:0
                        });
                    }
                }
            }
            //add first and last date
            var first_date = new Date(2012,6,1), last_date = new Date();
            last_date.setTime(last_date.getTime()+1000*60*60*24);
            dataset_line[k].frequency.push({date:first_date,count:0});
            dataset_line[k].frequency.push({date:last_date,count:0});
            dataset_line[k].frequency.sort(function(a,b){
                if(a.date< b.date) return -1;
                if(a.date >b.date) return 1;
                return 0;
            });
        }
        //Abbreviate name
        if (dataset_line[k].name.length > 15){
            dataset_line[k].name = dataset_line[k].name.substring(0,15) + ".";
        }
    }

    //Set time length
    var now = new Date();
    var one_week = new Date(), one_month = new Date(),
        three_months = new Date(), six_months = new Date(),
        twelve_months = new Date(), total = new Date(2012,6,1);

    one_week.setDate(now.getDate()-7);
    one_month.setDate(now.getDate()-30);
    three_months.setDate(now.getDate()-91);
    six_months.setDate(now.getDate()-183);
    twelve_months.setDate(now.getDate()-365);

    now = parseDate(monthNames[now.getMonth()] + "-" + now.getDate() + "-" +
        now.getFullYear());
    var temp = now;
    var two_days = 1000*60*60*48;
    now.setTime(temp.getTime()+two_days);
    one_week = parseDate(monthNames[one_week.getMonth()] + "-" +
        one_week.getDate() + "-" + one_week.getFullYear());
    one_month = parseDate(monthNames[one_month.getMonth()] + "-" +
        one_month.getDate() + "-" + one_month.getFullYear());
    three_months = parseDate(monthNames[three_months.getMonth()] + "-" +
        three_months.getDate() + "-" + three_months.getFullYear());
    six_months = parseDate(monthNames[six_months.getMonth()] + "-" +
        six_months.getDate() + "-" + six_months.getFullYear());
    twelve_months = parseDate(monthNames[twelve_months.getMonth()] + "-" +
        twelve_months.getDate() + "-" + twelve_months.getFullYear());
    total = parseDate(monthNames[total.getMonth()] + "-" +
        total.getDate() + "-" + total.getFullYear());

    var time_length = {
            one_week: [one_week, now],
            one_month:[one_month, now],
            three_months: [three_months, now],
            six_months: [six_months, now],
            twelve_months: [twelve_months, now],
            total: [total, now]
        };

    var color = d3.scale.category20();

    // Set x and y axis
    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, margin.top*0.4]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    //Append svg
    var svg_line = d3.select(container)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");

    //Show total as default
    var time = time_length.three_months;
    var position = [];
    redraw(time);

    //Change graph as user select
    var menu = d3.select(control)
        .on("change", change);

    function change() {
        var series = menu.property("value");
        var time = {
            "one-week": time_length.one_week,
            "one-month": time_length.one_month,
            "three-months": time_length.three_months,
            "six-months": time_length.six_months,
            "twelve-months": time_length.twelve_months,
            "total":time_length.total
        };
        position = [];
        redraw(time[series]);
    }

    //Draw function
    function redraw(time) {

        //Remove old graph
        svg_line.selectAll("path").remove();
        svg_line.selectAll("text").remove();
        svg_line.select(".x.axis").remove();

        var time_end = time[1];
        time_end.setTime(time[1].getTime()-1000*60*60);

        //Set "d" attr
        var line_init = d3.svg.line()
            .interpolate("linear")
            .x(function(d) {
                if (d.date>time[0] && d.date<(time_end)){
                    return x(d.date);
                }
                else {
                    return null;
                }
            })
            .y(height);
        var line = d3.svg.line()
            .interpolate("linear")
            .x(function(d) {
                if (d.date>time[0] && d.date<(time_end)){
                    return x(d.date);
                }
                else {
                    return null;
                }
            })
            .y(function(d) {
                if (d.date>time[0] && d.date<(time_end)){
                    return y(d.count);
                }
                else {
                    return height;
                }
            });

        //Reset label label
        svg_line.append("text")
            .attr("x", width-40)
            .attr("y", -15)
            .style("text-decoration","underline")
            .attr("class", "btn")
            .on("click", change)
            .text("Reset graph");

        //Set domain
        x.domain(d3.extent(time, function(d) { return d; }));
        y.domain([0,max_Y]);

        //Draw x and y axis
        //For IE 8 rotate issue
        if (isIE()!=false && isIE() < 9){
            svg_line.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis)
                .selectAll("text")
                .attr("class","x text")
                .style("text-anchor", "middle");
        }
        else{
            svg_line.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis)
                .selectAll("text")
                .attr("class","x text")
                .style("text-anchor", "end")
                .attr("transform", "rotate(-45)");
        }

        svg_line.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0.3*margin.left)
            .style("text-anchor", "end");

        //Draw lines
        for (var l=0; l<dataset_line.length; l++){

            if (dataset_line[l].frequency.length > 1){
                svg_line.append("path")
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
                //Find right largest position
                var j = 0,
                    max = dataset_line[l].frequency[0].count,
                    max_index = 0;

                while(++j < dataset_line[l].frequency.length) {
                    if(dataset_line[l].frequency[j].count >= max
                        && dataset_line[l].frequency[j].date > time[0]
                        && dataset_line[l].frequency[j].count != 0) {
                        max_index = j;
                        max = dataset_line[l].frequency[j].count;
                    }
                }
                // For IE 8 large number can cause error
                if (isIE()!=false && isIE() < 9){
                    if(y(dataset_line[l].frequency[max_index].count)<150){
                        svg_line.append("text")
                            .attr("transform", "translate("
                                + x(dataset_line[l].frequency[max_index].date)
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
                    svg_line.append("text")
                        .attr("transform", "translate("
                            + x(dataset_line[l].frequency[max_index].date) +
                            "," + y(dataset_line[l].frequency[max_index].count)
                            + ") rotate(-45)")
                        .attr("class", "legend btn")
                        .attr("fill", color(dataset_line[l].name))
                        .on("click", moveLabel)
                        .text(dataset_line[l].name);
                }
            }
        }
    }//end redraw function

    //move label function
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