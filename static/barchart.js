var _data_source = data_source;

var BarChart = {
  main: function() {
    var m = [30, 30, 10, 100];
    var w = 960 - m[1] - m[3];
    var h = 430 - m[0] - m[2];

    var format = d3.format(",.2f");

    var x = d3.scale.linear().range([0, w]),
        y = d3.scale.ordinal().rangeRoundBands([0, h], .1);

    var xAxis = d3.svg.axis().scale(x).orient("top").tickSize(-h),
        yAxis = d3.svg.axis().scale(y).orient("left").tickSize(0);

    var svg = d3.select("body").append("svg")
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2])
      .append("g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

    d3.csv(_data_source, function(data) {

      // Parse numbers, and sort by value.
      data.forEach(function(d) { d.value = +d.value; });
      // data.sort(function(a, b) { return b.value - a.value; });
      data.sort(function(a, b) {
        if (b.name > a.name) return 1;
        return -1;
      });

      // Set the scale domain.
      x.domain([0, d3.max(data, function(d) { return d.value; })]);
      y.domain(data.map(function(d) { return d.name; }));

      var bar = svg.selectAll("g.bar")
          .data(data)
        .enter().append("g")
          .attr("class", "bar")
          .attr("transform", function(d) { return "translate(0," + y(d.name) + ")"; });

      bar.append("rect")
          .attr("width", function(d) { return x(d.value); })
          .attr("height", y.rangeBand());

      bar.append("text")
          .attr("class", "value")
          .attr("x", function(d) { return x(d.value); })
          .attr("y", y.rangeBand() / 2)
          .attr("dx", -3)
          .attr("dy", ".35em")
          .attr("text-anchor", "end")
          .text(function(d) { return format(d.value); });

      svg.append("g")
          .attr("class", "x axis")
          .call(xAxis);

      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis);
    });
  }
};

BarChart.main();
