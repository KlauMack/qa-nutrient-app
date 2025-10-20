// daily_summary.js

// Collapse sections
function stryNS_9fa48() {
  var g = typeof globalThis === 'object' && globalThis && globalThis.Math === Math && globalThis || new Function("return this")();
  var ns = g.__stryker__ || (g.__stryker__ = {});
  if (ns.activeMutant === undefined && g.process && g.process.env && g.process.env.__STRYKER_ACTIVE_MUTANT__) {
    ns.activeMutant = g.process.env.__STRYKER_ACTIVE_MUTANT__;
  }
  function retrieveNS() {
    return ns;
  }
  stryNS_9fa48 = retrieveNS;
  return retrieveNS();
}
stryNS_9fa48();
function stryCov_9fa48() {
  var ns = stryNS_9fa48();
  var cov = ns.mutantCoverage || (ns.mutantCoverage = {
    static: {},
    perTest: {}
  });
  function cover() {
    var c = cov.static;
    if (ns.currentTestId) {
      c = cov.perTest[ns.currentTestId] = cov.perTest[ns.currentTestId] || {};
    }
    var a = arguments;
    for (var i = 0; i < a.length; i++) {
      c[a[i]] = (c[a[i]] || 0) + 1;
    }
  }
  stryCov_9fa48 = cover;
  cover.apply(null, arguments);
}
function stryMutAct_9fa48(id) {
  var ns = stryNS_9fa48();
  function isActive(id) {
    if (ns.activeMutant === id) {
      if (ns.hitCount !== void 0 && ++ns.hitCount > ns.hitLimit) {
        throw new Error('Stryker: Hit count limit reached (' + ns.hitCount + ')');
      }
      return true;
    }
    return false;
  }
  stryMutAct_9fa48 = isActive;
  return isActive(id);
}
document.querySelectorAll(stryMutAct_9fa48("0") ? "" : (stryCov_9fa48("0"), '.food-section-content')).forEach(content => {
  if (stryMutAct_9fa48("1")) {
    {}
  } else {
    stryCov_9fa48("1");
    if (stryMutAct_9fa48("4") ? content.children.length !== 0 : stryMutAct_9fa48("3") ? false : stryMutAct_9fa48("2") ? true : (stryCov_9fa48("2", "3", "4"), content.children.length === 0)) {
      if (stryMutAct_9fa48("5")) {
        {}
      } else {
        stryCov_9fa48("5");
        content.style.maxHeight = stryMutAct_9fa48("6") ? "" : (stryCov_9fa48("6"), '0px');
      }
    } else {
      if (stryMutAct_9fa48("7")) {
        {}
      } else {
        stryCov_9fa48("7");
        content.style.maxHeight = content.scrollHeight + (stryMutAct_9fa48("8") ? "" : (stryCov_9fa48("8"), 'px'));
      }
    }
  }
});
document.querySelectorAll(stryMutAct_9fa48("9") ? "" : (stryCov_9fa48("9"), '.food-section-toggle')).forEach(header => {
  if (stryMutAct_9fa48("10")) {
    {}
  } else {
    stryCov_9fa48("10");
    header.addEventListener(stryMutAct_9fa48("11") ? "" : (stryCov_9fa48("11"), 'click'), () => {
      if (stryMutAct_9fa48("12")) {
        {}
      } else {
        stryCov_9fa48("12");
        const content = header.nextElementSibling;
        const chevron = header.querySelector(stryMutAct_9fa48("13") ? "" : (stryCov_9fa48("13"), '.chevron-icon'));
        chevron.classList.toggle(stryMutAct_9fa48("14") ? "" : (stryCov_9fa48("14"), 'rotate-180'));
        if (stryMutAct_9fa48("17") ? content.style.maxHeight || content.style.maxHeight !== '0px' : stryMutAct_9fa48("16") ? false : stryMutAct_9fa48("15") ? true : (stryCov_9fa48("15", "16", "17"), content.style.maxHeight && (stryMutAct_9fa48("19") ? content.style.maxHeight === '0px' : stryMutAct_9fa48("18") ? true : (stryCov_9fa48("18", "19"), content.style.maxHeight !== (stryMutAct_9fa48("20") ? "" : (stryCov_9fa48("20"), '0px')))))) {
          if (stryMutAct_9fa48("21")) {
            {}
          } else {
            stryCov_9fa48("21");
            content.style.maxHeight = stryMutAct_9fa48("22") ? "" : (stryCov_9fa48("22"), '0px');
          }
        } else {
          if (stryMutAct_9fa48("23")) {
            {}
          } else {
            stryCov_9fa48("23");
            content.style.maxHeight = content.scrollHeight + (stryMutAct_9fa48("24") ? "" : (stryCov_9fa48("24"), 'px'));
          }
        }
      }
    });
  }
});

// Add food modal
const addModal = document.getElementById(stryMutAct_9fa48("25") ? "" : (stryCov_9fa48("25"), 'food-entry-modal'));
const addButtons = document.querySelectorAll(stryMutAct_9fa48("26") ? "" : (stryCov_9fa48("26"), '.add-food-btn'));
const addCancelBtn = document.getElementById(stryMutAct_9fa48("27") ? "" : (stryCov_9fa48("27"), 'cancel-food-btn'));
const addForm = document.getElementById(stryMutAct_9fa48("28") ? "" : (stryCov_9fa48("28"), 'food-entry-form'));
addButtons.forEach(btn => {
  if (stryMutAct_9fa48("29")) {
    {}
  } else {
    stryCov_9fa48("29");
    btn.addEventListener(stryMutAct_9fa48("30") ? "" : (stryCov_9fa48("30"), 'click'), e => {
      if (stryMutAct_9fa48("31")) {
        {}
      } else {
        stryCov_9fa48("31");
        e.stopPropagation();
        addForm.reset();
        addModal.classList.remove(stryMutAct_9fa48("32") ? "" : (stryCov_9fa48("32"), 'hidden'));
      }
    });
  }
});
addCancelBtn.addEventListener(stryMutAct_9fa48("33") ? "" : (stryCov_9fa48("33"), 'click'), () => {
  if (stryMutAct_9fa48("34")) {
    {}
  } else {
    stryCov_9fa48("34");
    addModal.classList.add(stryMutAct_9fa48("35") ? "" : (stryCov_9fa48("35"), 'hidden'));
  }
});

// Edit food modal
document.querySelectorAll(stryMutAct_9fa48("36") ? "" : (stryCov_9fa48("36"), '.food-item')).forEach(item => {
  if (stryMutAct_9fa48("37")) {
    {}
  } else {
    stryCov_9fa48("37");
    item.addEventListener(stryMutAct_9fa48("38") ? "" : (stryCov_9fa48("38"), 'click'), () => {
      if (stryMutAct_9fa48("39")) {
        {}
      } else {
        stryCov_9fa48("39");
        const editModal = document.getElementById(stryMutAct_9fa48("40") ? "" : (stryCov_9fa48("40"), 'food-edit-modal'));
        const editForm = document.getElementById(stryMutAct_9fa48("41") ? "" : (stryCov_9fa48("41"), 'food-edit-form'));
        editModal.classList.remove(stryMutAct_9fa48("42") ? "" : (stryCov_9fa48("42"), 'hidden'));
        editForm.querySelector(stryMutAct_9fa48("43") ? "" : (stryCov_9fa48("43"), '[name="food_id"]')).value = item.dataset.id;
        editForm.querySelector(stryMutAct_9fa48("44") ? "" : (stryCov_9fa48("44"), '[name="name"]')).value = item.dataset.name;
        editForm.querySelector(stryMutAct_9fa48("45") ? "" : (stryCov_9fa48("45"), '[name="calories"]')).value = item.dataset.calories;
        editForm.querySelector(stryMutAct_9fa48("46") ? "" : (stryCov_9fa48("46"), '[name="protein"]')).value = item.dataset.protein;
        editForm.querySelector(stryMutAct_9fa48("47") ? "" : (stryCov_9fa48("47"), '[name="carbs"]')).value = item.dataset.carbs;
        editForm.querySelector(stryMutAct_9fa48("48") ? "" : (stryCov_9fa48("48"), '[name="fat"]')).value = item.dataset.fat;
      }
    });
  }
});
document.getElementById(stryMutAct_9fa48("49") ? "" : (stryCov_9fa48("49"), 'cancel-edit-btn')).addEventListener(stryMutAct_9fa48("50") ? "" : (stryCov_9fa48("50"), 'click'), () => {
  if (stryMutAct_9fa48("51")) {
    {}
  } else {
    stryCov_9fa48("51");
    document.getElementById(stryMutAct_9fa48("52") ? "" : (stryCov_9fa48("52"), 'food-edit-modal')).classList.add(stryMutAct_9fa48("53") ? "" : (stryCov_9fa48("53"), 'hidden'));
  }
});