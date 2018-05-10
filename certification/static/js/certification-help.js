// Define the tour!
var tour = {
  id: "hello-hopscotch",
  steps: [
    {
      title: "Supplier",
      content: "Select the desired supplier",
      target: "id_supplier",
      placement: "bottom"
    },
    {
      title: "Certification Code",
      content: "Fill with the supplier certification code",
      target: "id_code",
      placement: "bottom"
    },
    {
      title: "Description",
      content: "Describe the product of the certification",
      target: "id_product_description",
      placement: "bottom"
    },
    {
      title: "Revision Number",
      content: "Insert the revision number",
      target: "id_revision_ECM",
      placement: "bottom"
    },
    {
      title: "Revision Last",
      content: "Insert the date of the last revision",
      target: "id_revision_last",
      placement: "bottom"
    },
    {
      title: "Planned Steps",
      content: "Insert the number of planned steps",
      target: "id_planned_steps",
      placement: "bottom"
    },
    {
      title: "Date",
      content: "Insert the date of the certification",
      target: "id_date",
      placement: "bottom"
    },
  ]
};

/* ========== */
/* TOUR SETUP */
/* ========== */
addClickListener = function(el, fn) {
  if (el.addEventListener) {
    el.addEventListener('click', fn, false);
  }
  else {
    el.attachEvent('onclick', fn);
  }
},

init = function() {
  var startBtnId = 'startTourBtn',
      calloutId = 'startTourCallout',
      mgr = hopscotch.getCalloutManager(),
      state = hopscotch.getState();

  if (state && state.indexOf('hello-hopscotch:') === 0) {
    // Already started the tour at some point!
  }
  else {
    // Looking at the page for the first(?) time.
    setTimeout(function() {
      mgr.createCallout({
        id: calloutId,
        target: startBtnId,
        placement: 'left',
        title: 'Take an example tour',
        content: 'In case of doubts click here!',
        arrowOffset: '-1.5px',
        width: 200
      });
    }, 100);
  }

  addClickListener(document.getElementById(startBtnId), function() {
    if (!hopscotch.isActive) {
      mgr.removeAllCallouts();
      hopscotch.startTour(tour);
    }
  });
};

init();