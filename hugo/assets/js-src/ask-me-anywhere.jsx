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

class SpacerManager extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'mouseSpacerIndex': null,
      'visibleSpacers': [],
      'expandedSpacers': [],
    }
    this.handleShow = this.handleShow.bind(this);
    this.handleHide = this.handleHide.bind(this);
    this.handleExpand = this.handleExpand.bind(this);
    this.handleCollapse = this.handleCollapse.bind(this);
    this.handleMouseMove = this.handleMouseMove.bind(this);
    this.handleDoubleClick = this.handleDoubleClick.bind(this);
  }

  handleShow(spacerIndex) {
    this.setState({
      'visibleSpacers': this.state.visibleSpacers.concat([spacerIndex])
    });
  }

  handleHide(spacerIndex) {
    this.setState({
      'visibleSpacers': this.state.visibleSpacers.filter(
          (item) => {return item != spacerIndex;}
      )
    });
  }

  handleExpand(spacerIndex) {
    this.setState({
      'expandedSpacers': this.state.expandedSpacers.concat([spacerIndex])
    });
  }

  handleCollapse(spacerIndex) {
    this.setState({
      'expandedSpacers': this.state.expandedSpacers.filter(
          (item) => {return item != spacerIndex;}
      )
    });
  }

  handleMouseMove(event) {
    const articleElements = this.props.articleElements;

    const mouseY = event.clientY;
    let found = false;
    articleElements.each((index, el) => {
      const clientRect = el.getBoundingClientRect();
      const top = clientRect.y;
      const bottom = top + clientRect.height;

      if (top == bottom) {
        return; // Skips style, script, etc.
      }

      let nextTop;
      if (index + 1 < articleElements.length) {
        const nextClientRect = articleElements[index + 1].getBoundingClientRect();
        nextTop = nextClientRect.y;
      } else {
        nextTop = Infinity;
      }

      if (mouseY > bottom - 40 && mouseY < nextTop + 40) {
        this.setState({
          'mouseSpacerIndex': index,
        });
        found = true;
      }
      // TODO(dbieber): Note this includes script tags from mailchimp.
    });
    if (!found) {
      this.setState({
        'mouseSpacerIndex': null,
      });
    }
  }

  handleDoubleClick(event) {
    const articleElements = this.props.articleElements;
    const mouseY = event.clientY;
    articleElements.each((index, el) => {
      const clientRect = el.getBoundingClientRect();
      const top = clientRect.y;
      const bottom = top + clientRect.height;

      if (mouseY > top && mouseY < bottom) {
        this.handleExpand(index);
      }
    });
  }

  handleClick(event) {
  }

  componentDidMount() {
    document.addEventListener('mousemove', this.handleMouseMove);
    document.addEventListener('dblclick', this.handleDoubleClick);
    document.addEventListener('click', this.handleClick);
  }
  componentWillUnmount() {
    document.removeEventListener('mousemove', this.handleMouseMove);
    document.removeEventListener('dblclick', this.handleDoubleClick);
    document.removeEventListener('click', this.handleClick);
  }

  render() {
    const spacers = [];
    const articleElements = this.props.articleElements;
    const spacerIndex = this.state.mouseSpacerIndex;

    const spacerIndexes = new Set(
      this.state.expandedSpacers
      .concat(this.state.visibleSpacers)
      .concat([spacerIndex])
    );
    spacerIndexes.forEach((index) => {
      if (index != null) {
        const div = this.props.divs[index];
        spacers.push(<SpacerPlacer
              key={index}
              preview={articleElements[index].textContent.slice(0, 250)}
              paragraphIndex={index}
              handleShow={this.handleShow}
              handleHide={this.handleHide}
              handleExpand={this.handleExpand}
              handleCollapse={this.handleCollapse}
              container={div}
              expanded={this.state.expandedSpacers.includes(index)}
              visible={true} />);
      } 
    });

    return <div>
      {spacers}
    </div>
  }
}

class SpacerPlacer extends React.Component {
  componentDidMount() {
    // Add Spacer at appropriate place.
    ReactDOM.render(<Spacer {...this.props} />, this.props.container);
  }
  componentDidUpdate(prevProps) {
    // Typical usage (don't forget to compare props):
    if (this.props !== prevProps) {
      ReactDOM.render(<Spacer {...this.props} />, this.props.container);
    }
  }
  componentWillUnmount() {
    // Remove Spacer from said place.
    ReactDOM.unmountComponentAtNode(this.props.container);
  }
  render() {
    return <span id={this.key}/>;
  }
}

class Spacer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      status: 'pending',
    }
    this.handleClick = this.handleClick.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleSuccess = this.handleSuccess.bind(this);
    this.handleFailure = this.handleFailure.bind(this);
    this.handleCancel = this.handleCancel.bind(this);
  }

  handleClick() {
    this.props.handleShow(this.props.paragraphIndex);
    this.props.handleExpand(this.props.paragraphIndex);
  }

  handleSubmit() {
    this.props.handleCollapse(this.props.paragraphIndex);
    this.setState({
      status: 'submit',
    });
  }
  handleSuccess() {
    this.props.handleCollapse(this.props.paragraphIndex);
    this.setState({
      status: 'success',
    });
  }
  handleFailure() {
    this.setState({
      status: 'failure',
    });
  }

  handleCancel(event) {
    this.props.handleCollapse(this.props.paragraphIndex);
    this.props.handleHide(this.props.paragraphIndex);
    this.setState({
      status: 'pending',
    });
    event.preventDefault();
  }

  render() {
    if (this.props.expanded) {
      return <CommentForm
          preview={this.props.preview}
          paragraphIndex={this.props.paragraphIndex}
          handleSubmit={this.handleSubmit}
          handleSuccess={this.handleSuccess}
          handleFailure={this.handleFailure}
          handleCancel={this.handleCancel}/>;
    }
    var text = {
      "pending": "Click to React.",
      "success": "Submitted successfully!",
      "failure": "Failed to submit; maybe just email me instead.",
      "submit": "Submitted!",
    }
    if (this.props.visible) {
      return (<span className="spacer" onClick={this.handleClick}>
        <span className="spacer-left" />
        <span className="spacer-center">
          {text[this.state.status]}
        </span>
        <span className="spacer-right" />
      </span>);
    }
    else {
      return null;
    }
  }
}

class CommentForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {email: '', comment: ''};

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
    event.preventDefault();

    this.props.handleSubmit();

    const handleSuccess = this.props.handleSuccess;
    const handleFailure = this.props.handleFailure;

    // Add a new comment entry to the database.
    firebase.firestore().collection('comments').add({
      comment: this.state.comment,
      context_preview: this.props.preview,
      email: this.state.email,
      paragraph: this.props.paragraphIndex,
      url: document.URL,
      status: "new",
      timestamp: firebase.firestore.FieldValue.serverTimestamp()
    }).then(function() {
      handleSuccess();
    }).catch(function(error) {
      handleFailure();
    });
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <textarea
            name="comment"
            style={{width: '100%'}}
            value={this.state.comment}
            placeholder="Ask away!"
            onChange={this.handleInputChange} />
        <input
            name="email"
            style={{width: '60%'}}
            type="text"
            placeholder="Email (optional)"
            value={this.state.email}
            onChange={this.handleInputChange} />
        <input
            type="submit"
            style={{width: '20%'}}
            value="Submit" />
        <button
            onClick={this.props.handleCancel}
            style={{width: '20%'}}>Cancel</button>
      </form>
    );
  }
}

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

const content = $('#article-content');
const articleElements = content.children();
const div = document.createElement('div');
$(div).insertAfter(content);

const divs = [];
articleElements.each((index, el) => {
  const div = document.createElement('div');
  $(div).insertAfter(el);
  divs.push(div);
});

ReactDOM.render(
  <SpacerManager articleElements={articleElements} divs={divs} />,
  div);


// Tooltip text:
// If you have any comments, questions, emojis, feelings, or want to talk about what you're reading,
// this is a great way to share that with the author!
// No thought is too trivial; please don't hesitate to leave a reaction or ask a question.
// Be sure to leave some contact info too if you'd like the author to be able to respond privately (Twitter, Email, FB, etc are all valid).
