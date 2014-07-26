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

    var last_week_data = my_data[0];
    var this_week_data = my_data[1];

    last_week_data.forEach(function(d) {
        d.date = d[0] / 60 / 60 / 24; //parseDate(d.date);
        d.balance = +d[1];//+d.balance;
    });
    this_week_data.forEach(function(d) {
        d.date = d[0] / 60 / 60 / 24; //parseDate(d.date);
        d.balance = +d[1];//+d.balance;
    });
    var merged_data = last_week_data.concat(this_week_data);

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
        .text("Balance ($)");

    svg.append("path")
        .datum(last_week_data)
        .attr("class", "greenline")
        .attr("d", line);

    svg.append("path")
        .datum(this_week_data)
        .attr("class", "line")
        .attr("d", line);

    console.log("Done");
  }
}

LineChartByDate.main(_data);
