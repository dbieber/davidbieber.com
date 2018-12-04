/** @jsx React.DOM */

// React D3 Components
var Chart = React.createClass({
  propTypes: {
    width: React.PropTypes.number.isRequired,
    height: React.PropTypes.number.isRequired
  },

  render: function() {
    return (
      <svg width={this.props.width} height={this.props.height}>{this.props.children}</svg>
    );
  }
});

var Bar = React.createClass({
  propTypes: {
    width: React.PropTypes.number.isRequired,
    height: React.PropTypes.number.isRequired,
    x: React.PropTypes.number.isRequired,
    y: React.PropTypes.number.isRequired,
    color: React.PropTypes.string
  },

  getDefaultProps: function() {
    return {
      width: 0,
      height: 0,
      x: 0,
      y: 0
    };
  },

  render: function() {
    return (
      <rect
        fill={this.props.color}
        width={this.props.width} height={this.props.height}
        x={this.props.x} y={this.props.y} />
    );
  }
});

var Line = React.createClass({
  getDefaultProps: function() {
    return {
      color: 'blue',
      width: 2
    };
  },

  render: function() {
    var path = d3.svg.line()
      .x(function(d) { return xScale(d.x); })
      .y(function(d) { return yScale(d.y); })
      .interpolate(this.props.interpolate);

    var data = this.props.data;

    return (
      <path
        d={path(data)}
        stroke={this.props.color}
        strokeWidth={this.props.width}
        fill="none" />
    );
  }
});

var BarChart = React.createClass({
  getDefaultProps: function() {
    return {
      color: 'blue'
    };
  },

  render: function() {
    var props = this.props;

    var yScale = d3.scale.linear()
      .domain([0, d3.max(this.props.data)])
      .range([0, this.props.height]);

    var xScale = d3.scale.ordinal()
      .domain(d3.range(this.props.data.length))
      .rangeRoundBands([0, this.props.width], 0.05);

    var bars = _.map(this.props.data, function(point, i) {
      return (
        <Bar height={yScale(point)} width={xScale.rangeBand()} x={xScale(i)} y={props.height - yScale(point)} color={props.color} key={i} />
      )
    });

    return <Chart height={this.props.height} width={this.props.width}>
      <g>{bars}</g>
    </Chart>;
  }
});

var LineChart = React.createClass({
  render: function() {
    var xScale = d3.scale.linear()
      .domain([0, 6])
      .range([0, this.props.width]);

    var yScale = d3.scale.linear()
      .domain([0, max])
      .range([this.props.height, 0]);

    return (
      <Chart width={this.props.width} height={this.props.height}>
      </Chart>
    );
  }
});

var CategoryBarChart = React.createClass({
  render: function() {
    return this.transferPropsTo(<BarChart></BarChart>);
  }
});

var BarChart = React.createClass({
  getDefaultProps: function() {
    return {
      color: 'blue'
    };
  },

  render: function() {
    var data = this.props.data;
    var props = this.props;

    var yScale = d3.scale.linear()
      .domain([0, d3.max(_.values(data))])
      .range([0, this.props.height]);

    var xScale = d3.scale.ordinal()
      .domain(d3.range(_.keys(data).length))
      .rangeRoundBands([0, this.props.width], 0.05);

    var i = 0;
    var bars = _.map(data, function(value, key) {
      return (
        <Bar height={yScale(value)} width={xScale.rangeBand()} x={xScale(i)} y={props.height - yScale(value)} color={props.color} key={i++} />
      );
    });

    return <Chart height={this.props.height} width={this.props.width}>
      <g>{bars}</g>
    </Chart>;
  }
});
