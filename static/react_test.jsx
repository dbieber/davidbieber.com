/** @jsx React.DOM */

var data = {
  series1: [ { x: 0, y: 20 }, { x: 1, y: 30 }, { x: 2, y: 10 }, { x: 3, y: 5 }, { x: 4, y: 8 }, { x: 5, y: 15 }, { x: 6, y: 10 } ],
  series2: [ { x: 0, y: 8 }, { x: 1, y: 5 }, { x: 2, y: 20 }, { x: 3, y: 12 }, { x: 4, y: 4 }, { x: 5, y: 6 }, { x: 6, y: 2 } ],
  series3: [ { x: 0, y: 0 }, { x: 1, y: 5 }, { x: 2, y: 8 }, { x: 3, y: 2 }, { x: 4, y: 6 }, { x: 5, y: 4 }, { x: 6, y: 2 } ]
};

var data = [ 30, 10, 5, 8, 15, 10 ];

// React.renderComponent(
//   <LineChart data={data} />,
//   document.getElementById('main')
// );


// React.renderComponent(
//   <StackedBarChart data={data} />,
//   document.getElementById('main')
// );

var data = {
    'Cash': 10,
    'Credit': 200,
    'Change': 5
};

React.renderComponent(
  <CategoryBarChart width={600} height={300} data={data} />,
  document.getElementById('main')
);
