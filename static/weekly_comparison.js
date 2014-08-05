/** @jsx React.DOM */
// Expects data = [last_week_data, this_week_data]
var _data = data;

var LineChartByDate = {
  main: function(my_data) {
    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var line = d3.svg.line()
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.balance); });

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var this_week_data = my_data[0];
    var last_week_data = my_data[1];
    var two_week_data = my_data[2];
    var three_week_data = my_data[3];

    var merged_data = [];
    for (week_id in my_data) {
        my_data[week_id].forEach(function(d) {
            d.date = d[0] / 60 / 60 / 24; //parseDate(d.date);
            d.balance = +d[1];//+d.balance;
        });
        merged_data = merged_data.concat(my_data[week_id]);
    }

    x.domain(d3.extent(merged_data, function(d) { return d.date; }));
    y.domain(d3.extent(merged_data, function(d) { return d.balance; }));

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Expenses ($)");

    // var colors = ["#4682B4", "#609CCE", "#79B5E7", "#93CFFF", "#ACE8FF", "#C5FFFF", "#DFFFFF", "#F9FFFF"];
    var colors = ["red", "orange", "gold", "green", "blue", "indigo"];
    var week_ids = [];
    for (week_id in my_data) {
        week_ids.push(week_id);
    }
    for (var i = 0; i < week_ids.length; i++) {
        var week_id = week_ids[week_ids.length - i - 1];
        console.log(week_id);
        if (!(week_id in colors)) continue;

        svg.append("path")
            .datum(my_data[week_id])
            .attr("class", "line")
            .style("stroke", colors[week_id])
            .attr("d", line);
    }
  }
}

LineChartByDate.main(_data);
