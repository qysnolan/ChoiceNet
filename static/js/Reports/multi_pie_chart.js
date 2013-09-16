/*	
	Uses the given container to draw a pie chart.
	datasets is an array of datasets to cycle through.
	Each dataset is an array with two elements: the first being the title of
	the graph, the second an array of slices.
	Each slice is an array with two elements: the first being the label for
	that slice, the second the value/size of the slice.
*/
function multiPieChart(container, datasets, title, chart_width) {
	var width = chart_width,
		height = chart_width - 5,
		radius = Math.min(width, height) / 3,
		padding = 20,
		pie_update_duration = 500,
		pie_view_duration = 2000;

	var textOffset = 18;

	pie_view_duration += pie_update_duration;

	var blue_color = d3.scale.linear().
        domain([0,6]).
        range(["#44ccff","#002266"]);
	
	var arc = d3.svg.arc()
						.outerRadius(radius - 10)
						.innerRadius(width / 8);
	
	var pie = d3.layout.pie()
        .sort(null)
        .value(function(d) { return d.count; });
	
	var svg_pie = d3.select(container).append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform",
                "translate(" + width/2 + "," + ((height/2)+padding) + ")"
            );
					
	var arc_grp = svg_pie.append("g")
		    .attr("class", "arcGrp");

	var label_group = svg_pie.append("g")
		    .attr("class", "label_group");

	var title_group = svg_pie.append("g")
		    .attr("class", "title_group");

	svg_pie.append("text")
		.attr("font-size", "16px")
		.attr("x", 0)
		.attr("y", padding-(height/2))
		.attr("text-anchor", "middle")
		.text(title);

	function convert_dist(data) {
		var converted = [];
		data.forEach(function(d) {
            if (d[1]!=0){
                converted.push({category:d[0],count:d[1]});
            }
		});
		return converted.reverse();
	}

	function convert_data(datasets) {
		var converted = [];
		datasets.forEach(function(d) {
			var dist = convert_dist(d[1]);
			converted.push({ title:d[0], distribution:dist });
		});
		return converted;
	}

	datasets = convert_data(datasets);

	// Transitions to the next dataset
	var update_pie_chart = function(dataset_index) {
		cur_dataset = datasets[dataset_index];
		dataset = cur_dataset.distribution;
		title = [cur_dataset.title];

		var t = title_group.selectAll("text").data(title);

		t.enter()
			.append("text")
           .attr("x", 0)
           .attr("y", padding+20-(height/2))
           .attr("text-anchor", "middle")
           .style("font-size", "14px");

        if (dataset.length!=0){
            t.text(title);
        }
        else{
            t.text("No Evaluation for " + title);
        }

        t.exit().remove();


		paths = arc_grp.selectAll("path").data(pie(dataset));

		paths.enter()
			.append("path")
			.attr("stroke", "white")
			.attr("stroke-width", 0.8)
			.attr("fill", function(d, i) { return blue_color(i); })
			.transition()
				.duration(pie_update_duration)
				.attrTween("d", arcTween);

		paths
			.transition()
				.duration(pie_update_duration)
				.attrTween("d", arcTween);

		paths.exit()
			.transition()
				.duration(pie_update_duration)
				.attrTween("d", removeArcTween)
			.remove();

		//DRAW LABELS WITH ENTITY NAMES
		var nameLabels = label_group.selectAll("text.units").
                data(pie(dataset));

		nameLabels.enter().append("text")
			.attr("class", "units")
			.attr("text-anchor", "middle")
			.style("font-size", "12px");

		nameLabels
			.text(function(d){
				if (d.data.count > 0) {
					return d.data.category;		
				} else {
					return ""
				}})
			.transition().
            duration(pie_update_duration).
            attrTween("transform", textTween);

		nameLabels.exit().remove();
	}; // end update function

	// Used to transition pie slices
	var arcTween = function(a) {
		if (!this._previous) {
			var middle = (a.startAngle + a.endAngle) / 2.0;
			this._previous = {startAngle:middle, endAngle:middle}
		}
		var i = d3.interpolate(this._previous, a);
		this._previous = i(0);
		return function(t) { return arc(i(t)); };
	};

	// Used to remove pie slices
	function removeArcTween(d, i) {
		s0 = 2 * Math.PI;
		e0 = 2 * Math.PI;
		var i = d3.interpolate(this._previous, {startAngle: s0, endAngle: e0});
		return function(t) {
			var b = i(t);
			return arc(b);
		};
	}

	// Used to transition slice labels
	function textTween(d) {
		if (! this._previous) {
			this._previous = 0;
		}
		var now = (d.startAngle + d.endAngle - Math.PI) / 2.0;
		
		var fn = d3.interpolateNumber(this._previous, now);
		this._previous = now;
		return function(t) {
			var val = fn(t);
			return "translate(" + Math.cos(val) * (radius+textOffset) + "," +
                Math.sin(val) * (radius+textOffset) + ")";
		};
	}
		
	// Display the first dataset
	var cur_index = 0;
	update_pie_chart(cur_index);
	
	// Update the pie chart at regular interval
	setInterval(function() {
		update_pie_chart(cur_index);
		cur_index++;
		cur_index = cur_index % datasets.length;
	}, pie_view_duration);

} // end multiPieChart function
