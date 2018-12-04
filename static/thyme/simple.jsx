/** @jsx React.DOM */
// Expects data
var _data = data;

(function(data) {
    var cash = data['cash'];
    var change = data['change'];
    var spent_today = data['spent_today'];

    var MoneyOutput = React.createClass({
        render: function() {
            var output = numeral(this.props.children).format('$0,0.00');
            return this.transferPropsTo(<span>{output}</span>);
        }
    });

    var NumberAndTextDisplay = React.createClass({
        render: function() {
            var number = this.props.number;
            var text = this.props.text;

            return <pre><div className="NumberTextDisplay">
                <MoneyOutput className="number">{number}</MoneyOutput>{" "}
                <span className="text">{text}</span>
            </div></pre>;
        }
    });

    React.renderComponent(
        <div>
            <NumberAndTextDisplay number={spent_today} text={"spent today."} />
            <NumberAndTextDisplay number={cash} text={"in your pocket."} />
            <NumberAndTextDisplay number={change} text={"on your desk."} />
        </div>,
        document.getElementById('main')
    );
})(_data);
