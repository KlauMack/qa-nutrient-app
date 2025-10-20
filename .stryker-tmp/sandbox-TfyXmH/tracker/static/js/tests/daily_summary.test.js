/**
 * @jest-environment jsdom
 */function stryNS_9fa48() {
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
describe(stryMutAct_9fa48("54") ? "" : (stryCov_9fa48("54"), 'daily_summary.js behaviors'), () => {
  if (stryMutAct_9fa48("55")) {
    {}
  } else {
    stryCov_9fa48("55");
    const scriptPath = stryMutAct_9fa48("56") ? "" : (stryCov_9fa48("56"), '../daily_summary.js');
    beforeEach(() => {
      if (stryMutAct_9fa48("57")) {
        {}
      } else {
        stryCov_9fa48("57");
        // Reset modules so requiring daily_summary.js runs fresh each test
        jest.resetModules();
        // Provide a minimal DOM that the script expects so it doesn't throw at load time
        document.body.innerHTML = stryMutAct_9fa48("58") ? `` : (stryCov_9fa48("58"), `
        <!-- Add-food modal and controls (script expects these ids) -->
        <div id="food-entry-modal" class="hidden">
          <form id="food-entry-form">
            <input name="name" />
          </form>
        </div>
        <button id="cancel-food-btn">Cancel Add</button>
        <button class="add-food-btn">Add</button>
  
        <!-- Edit-food modal and controls (script expects these ids) -->
        <div id="food-edit-modal" class="hidden">
          <form id="food-edit-form">
            <input name="food_id" />
            <input name="name" />
            <input name="calories" />
            <input name="protein" />
            <input name="carbs" />
            <input name="fat" />
          </form>
        </div>
        <button id="cancel-edit-btn">Cancel Edit</button>
  
        <!-- A header toggle and two contents for collapse tests -->
        <div class="food-section-toggle">
          <span class="chevron-icon"></span>
        </div>
        <div class="food-section-content" id="content-empty"></div>
  
        <div class="food-section-toggle">
          <span class="chevron-icon"></span>
        </div>
        <div class="food-section-content" id="content-nonempty">
          <div class="child">child</div>
        </div>
  
        <!-- A food item for editing -->
        <div class="food-item" data-id="42" data-name="Banana" data-calories="100" data-protein="1" data-carbs="27" data-fat="0.3"></div>
      `);
      }
    });
    test(stryMutAct_9fa48("59") ? "" : (stryCov_9fa48("59"), 'initializes collapse sections: empty content -> maxHeight 0px; non-empty -> scrollHeight px'), () => {
      if (stryMutAct_9fa48("60")) {
        {}
      } else {
        stryCov_9fa48("60");
        // Make content-nonempty report a scrollHeight of 150
        const contentNonEmpty = document.getElementById(stryMutAct_9fa48("61") ? "" : (stryCov_9fa48("61"), 'content-nonempty'));
        Object.defineProperty(contentNonEmpty, stryMutAct_9fa48("62") ? "" : (stryCov_9fa48("62"), 'scrollHeight'), stryMutAct_9fa48("63") ? {} : (stryCov_9fa48("63"), {
          configurable: stryMutAct_9fa48("64") ? false : (stryCov_9fa48("64"), true),
          get: stryMutAct_9fa48("65") ? () => undefined : (stryCov_9fa48("65"), () => 150)
        }));

        // Now require the script so it runs the initialization logic against the DOM
        require(scriptPath);
        const contentEmpty = document.getElementById(stryMutAct_9fa48("66") ? "" : (stryCov_9fa48("66"), 'content-empty'));
        expect(contentEmpty.style.maxHeight).toBe(stryMutAct_9fa48("67") ? "" : (stryCov_9fa48("67"), '0px'));
        expect(contentNonEmpty.style.maxHeight).toBe(stryMutAct_9fa48("68") ? "" : (stryCov_9fa48("68"), '150px'));
      }
    });
    test(stryMutAct_9fa48("69") ? "" : (stryCov_9fa48("69"), 'clicking a .food-item opens edit modal and populates form fields'), () => {
      if (stryMutAct_9fa48("70")) {
        {}
      } else {
        stryCov_9fa48("70");
        // Ensure edit modal and form exist (they do from beforeEach)
        const editModal = document.getElementById(stryMutAct_9fa48("71") ? "" : (stryCov_9fa48("71"), 'food-edit-modal'));
        const editForm = document.getElementById(stryMutAct_9fa48("72") ? "" : (stryCov_9fa48("72"), 'food-edit-form'));

        // Sanity: modal should start hidden
        expect(editModal.classList.contains(stryMutAct_9fa48("73") ? "" : (stryCov_9fa48("73"), 'hidden'))).toBe(stryMutAct_9fa48("74") ? false : (stryCov_9fa48("74"), true));

        // Load the script to attach event listeners
        require(scriptPath);

        // Find the item and simulate click
        const item = document.querySelector(stryMutAct_9fa48("75") ? "" : (stryCov_9fa48("75"), '.food-item'));
        item.click();

        // Modal should be visible (hidden class removed)
        expect(editModal.classList.contains(stryMutAct_9fa48("76") ? "" : (stryCov_9fa48("76"), 'hidden'))).toBe(stryMutAct_9fa48("77") ? true : (stryCov_9fa48("77"), false));

        // Inputs should be populated from dataset
        expect(editForm.querySelector(stryMutAct_9fa48("78") ? "" : (stryCov_9fa48("78"), '[name="food_id"]')).value).toBe(stryMutAct_9fa48("79") ? "" : (stryCov_9fa48("79"), '42'));
        expect(editForm.querySelector(stryMutAct_9fa48("80") ? "" : (stryCov_9fa48("80"), '[name="name"]')).value).toBe(stryMutAct_9fa48("81") ? "" : (stryCov_9fa48("81"), 'Banana'));
        expect(editForm.querySelector(stryMutAct_9fa48("82") ? "" : (stryCov_9fa48("82"), '[name="calories"]')).value).toBe(stryMutAct_9fa48("83") ? "" : (stryCov_9fa48("83"), '100'));
        expect(editForm.querySelector(stryMutAct_9fa48("84") ? "" : (stryCov_9fa48("84"), '[name="protein"]')).value).toBe(stryMutAct_9fa48("85") ? "" : (stryCov_9fa48("85"), '1'));
        expect(editForm.querySelector(stryMutAct_9fa48("86") ? "" : (stryCov_9fa48("86"), '[name="carbs"]')).value).toBe(stryMutAct_9fa48("87") ? "" : (stryCov_9fa48("87"), '27'));
        expect(editForm.querySelector(stryMutAct_9fa48("88") ? "" : (stryCov_9fa48("88"), '[name="fat"]')).value).toBe(stryMutAct_9fa48("89") ? "" : (stryCov_9fa48("89"), '0.3'));
      }
    });
  }
});