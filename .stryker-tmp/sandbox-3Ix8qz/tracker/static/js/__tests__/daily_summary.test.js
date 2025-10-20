/**
 * @jest-environment jsdom
 */

describe('daily_summary.js behaviors', () => {
    const scriptPath = '../daily_summary.js';
  
    beforeEach(() => {
      // Reset modules so requiring daily_summary.js runs fresh each test
      jest.resetModules();
      // Provide a minimal DOM that the script expects so it doesn't throw at load time
      document.body.innerHTML = `
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
      `;
    });
  
    test('initializes collapse sections: empty content -> maxHeight 0px; non-empty -> scrollHeight px', () => {
      // Make content-nonempty report a scrollHeight of 150
      const contentNonEmpty = document.getElementById('content-nonempty');
      Object.defineProperty(contentNonEmpty, 'scrollHeight', {
        configurable: true,
        get: () => 150,
      });
  
      // Now require the script so it runs the initialization logic against the DOM
      require(scriptPath);
  
      const contentEmpty = document.getElementById('content-empty');
  
      expect(contentEmpty.style.maxHeight).toBe('0px');
      expect(contentNonEmpty.style.maxHeight).toBe('150px');
    });
  
    test('clicking a .food-item opens edit modal and populates form fields', () => {
      // Ensure edit modal and form exist (they do from beforeEach)
      const editModal = document.getElementById('food-edit-modal');
      const editForm = document.getElementById('food-edit-form');
  
      // Sanity: modal should start hidden
      expect(editModal.classList.contains('hidden')).toBe(true);
  
      // Load the script to attach event listeners
      require(scriptPath);
  
      // Find the item and simulate click
      const item = document.querySelector('.food-item');
      item.click();
  
      // Modal should be visible (hidden class removed)
      expect(editModal.classList.contains('hidden')).toBe(false);
  
      // Inputs should be populated from dataset
      expect(editForm.querySelector('[name="food_id"]').value).toBe('42');
      expect(editForm.querySelector('[name="name"]').value).toBe('Banana');
      expect(editForm.querySelector('[name="calories"]').value).toBe('100');
      expect(editForm.querySelector('[name="protein"]').value).toBe('1');
      expect(editForm.querySelector('[name="carbs"]').value).toBe('27');
      expect(editForm.querySelector('[name="fat"]').value).toBe('0.3');
    });
  });