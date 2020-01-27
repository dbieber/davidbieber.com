'use strict';

// Render a non-visible Spacer after every paragraph.
// Register events on the articleElements for mousemove and doubleclick
// Listen for events on visible collapsed spacers for click
// On mousemove, make up to one spacer visible-collapsed (keep expanded spacers visible)
// On doubleclick, make a spacer visible-collapsed (dismiss/reopen if already submitted)
// On click, make visible-collapsed spacer visible-expanded.
// On submit, submit...

// Next let's try:
// Switching to a single component, SpacerManager
// with no Spacers at the Start.
// SpacerManager will listen to events

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var SpacerManager = function (_React$Component) {
  _inherits(SpacerManager, _React$Component);

  function SpacerManager(props) {
    _classCallCheck(this, SpacerManager);

    var _this = _possibleConstructorReturn(this, (SpacerManager.__proto__ || Object.getPrototypeOf(SpacerManager)).call(this, props));

    _this.state = {
      'mouseSpacerIndex': null,
      'visibleSpacers': [],
      'expandedSpacers': []
    };
    _this.handleShow = _this.handleShow.bind(_this);
    _this.handleHide = _this.handleHide.bind(_this);
    _this.handleExpand = _this.handleExpand.bind(_this);
    _this.handleCollapse = _this.handleCollapse.bind(_this);
    _this.handleMouseMove = _this.handleMouseMove.bind(_this);
    _this.handleDoubleClick = _this.handleDoubleClick.bind(_this);
    return _this;
  }

  _createClass(SpacerManager, [{
    key: 'handleShow',
    value: function handleShow(spacerIndex) {
      this.setState({
        'visibleSpacers': this.state.visibleSpacers.concat([spacerIndex])
      });
    }
  }, {
    key: 'handleHide',
    value: function handleHide(spacerIndex) {
      this.setState({
        'visibleSpacers': this.state.visibleSpacers.filter(function (item) {
          return item != spacerIndex;
        })
      });
    }
  }, {
    key: 'handleExpand',
    value: function handleExpand(spacerIndex) {
      this.setState({
        'expandedSpacers': this.state.expandedSpacers.concat([spacerIndex])
      });
    }
  }, {
    key: 'handleCollapse',
    value: function handleCollapse(spacerIndex) {
      this.setState({
        'expandedSpacers': this.state.expandedSpacers.filter(function (item) {
          return item != spacerIndex;
        })
      });
    }
  }, {
    key: 'handleMouseMove',
    value: function handleMouseMove(event) {
      var _this2 = this;

      var articleElements = this.props.articleElements;

      var mouseY = event.clientY;
      var found = false;
      articleElements.each(function (index, el) {
        var clientRect = el.getBoundingClientRect();
        var top = clientRect.y;
        var bottom = top + clientRect.height;

        if (top == bottom) {
          return; // Skips style, script, etc.
        }

        var nextTop = void 0;
        if (index + 1 < articleElements.length) {
          var nextClientRect = articleElements[index + 1].getBoundingClientRect();
          nextTop = nextClientRect.y;
        } else {
          nextTop = Infinity;
        }

        if (mouseY > bottom - 40 && mouseY < nextTop + 40) {
          _this2.setState({
            'mouseSpacerIndex': index
          });
          found = true;
        }
        // TODO(dbieber): Note this includes script tags from mailchimp.
      });
      if (!found) {
        this.setState({
          'mouseSpacerIndex': null
        });
      }
    }
  }, {
    key: 'handleDoubleClick',
    value: function handleDoubleClick(event) {
      var _this3 = this;

      var articleElements = this.props.articleElements;
      var mouseY = event.clientY;
      articleElements.each(function (index, el) {
        var clientRect = el.getBoundingClientRect();
        var top = clientRect.y;
        var bottom = top + clientRect.height;

        if (mouseY > top && mouseY < bottom) {
          _this3.handleExpand(index);
        }
      });
    }
  }, {
    key: 'handleClick',
    value: function handleClick(event) {}
  }, {
    key: 'componentDidMount',
    value: function componentDidMount() {
      document.addEventListener('mousemove', this.handleMouseMove);
      document.addEventListener('dblclick', this.handleDoubleClick);
      document.addEventListener('click', this.handleClick);
    }
  }, {
    key: 'componentWillUnmount',
    value: function componentWillUnmount() {
      document.removeEventListener('mousemove', this.handleMouseMove);
      document.removeEventListener('dblclick', this.handleDoubleClick);
      document.removeEventListener('click', this.handleClick);
    }
  }, {
    key: 'render',
    value: function render() {
      var _this4 = this;

      var spacers = [];
      var articleElements = this.props.articleElements;
      var spacerIndex = this.state.mouseSpacerIndex;

      var spacerIndexes = new Set(this.state.expandedSpacers.concat(this.state.visibleSpacers).concat([spacerIndex]));
      spacerIndexes.forEach(function (index) {
        if (index != null) {
          var _div = _this4.props.divs[index];
          spacers.push(React.createElement(SpacerPlacer, {
            key: index,
            preview: articleElements[index].textContent.slice(0, 250),
            paragraphIndex: index,
            handleShow: _this4.handleShow,
            handleHide: _this4.handleHide,
            handleExpand: _this4.handleExpand,
            handleCollapse: _this4.handleCollapse,
            container: _div,
            expanded: _this4.state.expandedSpacers.includes(index),
            visible: true }));
        }
      });

      return React.createElement(
        'div',
        null,
        spacers
      );
    }
  }]);

  return SpacerManager;
}(React.Component);

var SpacerPlacer = function (_React$Component2) {
  _inherits(SpacerPlacer, _React$Component2);

  function SpacerPlacer() {
    _classCallCheck(this, SpacerPlacer);

    return _possibleConstructorReturn(this, (SpacerPlacer.__proto__ || Object.getPrototypeOf(SpacerPlacer)).apply(this, arguments));
  }

  _createClass(SpacerPlacer, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      // Add Spacer at appropriate place.
      ReactDOM.render(React.createElement(Spacer, this.props), this.props.container);
    }
  }, {
    key: 'componentDidUpdate',
    value: function componentDidUpdate(prevProps) {
      // Typical usage (don't forget to compare props):
      if (this.props !== prevProps) {
        ReactDOM.render(React.createElement(Spacer, this.props), this.props.container);
      }
    }
  }, {
    key: 'componentWillUnmount',
    value: function componentWillUnmount() {
      // Remove Spacer from said place.
      ReactDOM.unmountComponentAtNode(this.props.container);
    }
  }, {
    key: 'render',
    value: function render() {
      return React.createElement('span', { id: this.key });
    }
  }]);

  return SpacerPlacer;
}(React.Component);

var Spacer = function (_React$Component3) {
  _inherits(Spacer, _React$Component3);

  function Spacer(props) {
    _classCallCheck(this, Spacer);

    var _this6 = _possibleConstructorReturn(this, (Spacer.__proto__ || Object.getPrototypeOf(Spacer)).call(this, props));

    _this6.state = {
      status: 'pending'
    };
    _this6.handleClick = _this6.handleClick.bind(_this6);
    _this6.handleSubmit = _this6.handleSubmit.bind(_this6);
    _this6.handleSuccess = _this6.handleSuccess.bind(_this6);
    _this6.handleFailure = _this6.handleFailure.bind(_this6);
    _this6.handleCancel = _this6.handleCancel.bind(_this6);
    return _this6;
  }

  _createClass(Spacer, [{
    key: 'handleClick',
    value: function handleClick() {
      this.props.handleShow(this.props.paragraphIndex);
      this.props.handleExpand(this.props.paragraphIndex);
    }
  }, {
    key: 'handleSubmit',
    value: function handleSubmit() {
      this.props.handleCollapse(this.props.paragraphIndex);
      this.setState({
        status: 'submit'
      });
    }
  }, {
    key: 'handleSuccess',
    value: function handleSuccess() {
      this.props.handleCollapse(this.props.paragraphIndex);
      this.setState({
        status: 'success'
      });
    }
  }, {
    key: 'handleFailure',
    value: function handleFailure() {
      this.setState({
        status: 'failure'
      });
    }
  }, {
    key: 'handleCancel',
    value: function handleCancel(event) {
      this.props.handleCollapse(this.props.paragraphIndex);
      this.props.handleHide(this.props.paragraphIndex);
      this.setState({
        status: 'pending'
      });
      event.preventDefault();
    }
  }, {
    key: 'render',
    value: function render() {
      if (this.props.expanded) {
        return React.createElement(CommentForm, {
          preview: this.props.preview,
          paragraphIndex: this.props.paragraphIndex,
          handleSubmit: this.handleSubmit,
          handleSuccess: this.handleSuccess,
          handleFailure: this.handleFailure,
          handleCancel: this.handleCancel });
      }
      var text = {
        "pending": "Click to React.",
        "success": "Submitted successfully!",
        "failure": "Failed to submit; maybe just email me instead.",
        "submit": "Submitted!"
      };
      if (this.props.visible) {
        return React.createElement(
          'span',
          { className: 'spacer', onClick: this.handleClick },
          React.createElement('span', { className: 'spacer-left' }),
          React.createElement(
            'span',
            { className: 'spacer-center' },
            text[this.state.status]
          ),
          React.createElement('span', { className: 'spacer-right' })
        );
      } else {
        return null;
      }
    }
  }]);

  return Spacer;
}(React.Component);

var CommentForm = function (_React$Component4) {
  _inherits(CommentForm, _React$Component4);

  function CommentForm(props) {
    _classCallCheck(this, CommentForm);

    var _this7 = _possibleConstructorReturn(this, (CommentForm.__proto__ || Object.getPrototypeOf(CommentForm)).call(this, props));

    _this7.state = { email: '', comment: '' };

    _this7.handleInputChange = _this7.handleInputChange.bind(_this7);
    _this7.handleSubmit = _this7.handleSubmit.bind(_this7);
    return _this7;
  }

  _createClass(CommentForm, [{
    key: 'handleInputChange',
    value: function handleInputChange(event) {
      var target = event.target;
      var value = target.type === 'checkbox' ? target.checked : target.value;
      var name = target.name;

      this.setState(_defineProperty({}, name, value));
    }
  }, {
    key: 'handleSubmit',
    value: function handleSubmit(event) {
      event.preventDefault();

      this.props.handleSubmit();

      var handleSuccess = this.props.handleSuccess;
      var handleFailure = this.props.handleFailure;

      // Add a new comment entry to the database.
      firebase.firestore().collection('comments').add({
        comment: this.state.comment,
        context_preview: this.props.preview,
        email: this.state.email,
        paragraph: this.props.paragraphIndex,
        url: document.URL,
        status: "new",
        timestamp: firebase.firestore.FieldValue.serverTimestamp()
      }).then(function () {
        handleSuccess();
      }).catch(function (error) {
        handleFailure();
      });
    }
  }, {
    key: 'render',
    value: function render() {
      return React.createElement(
        'form',
        { onSubmit: this.handleSubmit },
        React.createElement('textarea', {
          name: 'comment',
          style: { width: '100%' },
          value: this.state.comment,
          placeholder: 'Ask away!',
          onChange: this.handleInputChange }),
        React.createElement('input', {
          name: 'email',
          style: { width: '60%' },
          type: 'text',
          placeholder: 'Email (optional)',
          value: this.state.email,
          onChange: this.handleInputChange }),
        React.createElement('input', {
          type: 'submit',
          style: { width: '20%' },
          value: 'Submit' }),
        React.createElement(
          'button',
          {
            onClick: this.props.handleCancel,
            style: { width: '20%' } },
          'Cancel'
        )
      );
    }
  }]);

  return CommentForm;
}(React.Component);

function getSelectionText() {
  var text = "";
  if (window.getSelection) {
    text = window.getSelection().toString();
  } else if (document.selection && document.selection.type != "Control") {
    text = document.selection.createRange().text;
  }
  return text;
}

// 1. On mouse movement, turn on the in-between section closest to mouse
// 2. On double click on paragraph or single click on active in-between section,
// open in between section.

var content = $('#article-content');
var articleElements = content.children();
var div = document.createElement('div');
$(div).insertAfter(content);

var divs = [];
articleElements.each(function (index, el) {
  var div = document.createElement('div');
  $(div).insertAfter(el);
  divs.push(div);
});

ReactDOM.render(React.createElement(SpacerManager, { articleElements: articleElements, divs: divs }), div);

// Tooltip text:
// If you have any comments, questions, emojis, feelings, or want to talk about what you're reading,
// this is a great way to share that with the author!
// No thought is too trivial; please don't hesitate to leave a reaction or ask a question.
// Be sure to leave some contact info too if you'd like the author to be able to respond privately (Twitter, Email, FB, etc are all valid).