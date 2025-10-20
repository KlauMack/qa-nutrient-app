// daily_summary.js
// Refactored for improved readability, safety, and accessibility.

(function () {
    'use strict';
  
    // Selectors / constants
    const SELECTORS = {
      foodSectionContent: '.food-section-content',
      foodSectionToggle: '.food-section-toggle',
      chevronIcon: '.chevron-icon',
      addFoodModal: 'food-entry-modal',
      addFoodBtn: '.add-food-btn',
      cancelAddBtn: 'cancel-food-btn',
      addForm: 'food-entry-form',
      foodItem: '.food-item',
      editFoodModal: 'food-edit-modal',
      editForm: 'food-edit-form',
      cancelEditBtn: 'cancel-edit-btn',
    };
  
    /**
     * Safely get element by id
     * @param {string} id
     * @returns {HTMLElement|null}
     */
    function $id(id) {
      return document.getElementById(id) || null;
    }
  
    /**
     * Toggle a modal open/closed by id (adds/removes `hidden` class).
     * Also sets inert/aria-hidden for accessibility if supported.
     * @param {HTMLElement} modalEl
     * @param {boolean} open
     */
    function toggleModal(modalEl, open) {
      if (!modalEl) return;
      if (open) {
        modalEl.classList.remove('hidden');
        modalEl.setAttribute('aria-hidden', 'false');
        try {
          modalEl.removeAttribute('inert');
        } catch (e) {
          // inert may not be supported; ignore
        }
      } else {
        modalEl.classList.add('hidden');
        modalEl.setAttribute('aria-hidden', 'true');
        try {
          modalEl.setAttribute('inert', '');
        } catch (e) {
          // ignore
        }
      }
    }
  
    /**
     * Initialize collapsible sections with accessible toggles.
     */
    function initCollapsibleSections() {
      const contents = document.querySelectorAll(SELECTORS.foodSectionContent);
      contents.forEach((content) => {
        // Ensure maxHeight is set based on children
        if (!content || content.children.length === 0) {
          content.style.maxHeight = '0px';
          content.setAttribute('aria-hidden', 'true');
        } else {
          // Use scrollHeight so it expands to show content
          content.style.maxHeight = `${content.scrollHeight}px`;
          content.setAttribute('aria-hidden', 'false');
        }
      });
  
      const toggles = document.querySelectorAll(SELECTORS.foodSectionToggle);
      toggles.forEach((header) => {
        // make the header keyboard accessible if not a button
        if (header && header.getAttribute('role') === null) {
          header.setAttribute('role', 'button');
          header.setAttribute('tabindex', '0');
        }
  
        const onToggle = (evt) => {
          // Support both click and keyboard activation (Enter/Space)
          if (evt.type === 'keydown' && evt.key !== 'Enter' && evt.key !== ' ') return;
          evt.preventDefault();
  
          const content = header.nextElementSibling;
          const chevron = header.querySelector(SELECTORS.chevronIcon);
  
          const isOpen = content && content.style.maxHeight && content.style.maxHeight !== '0px';
  
          if (chevron) {
            chevron.classList.toggle('rotate-180', !isOpen);
          }
  
          if (!content) return;
  
          if (isOpen) {
            content.style.maxHeight = '0px';
            content.setAttribute('aria-hidden', 'true');
            header.setAttribute('aria-expanded', 'false');
          } else {
            // Recalculate scrollHeight in case content changed
            content.style.maxHeight = `${content.scrollHeight}px`;
            content.setAttribute('aria-hidden', 'false');
            header.setAttribute('aria-expanded', 'true');
          }
        };
  
        header.addEventListener('click', onToggle);
        header.addEventListener('keydown', onToggle);
      });
    }
  
    /**
     * Initialize Add Food modal: openers, cancel button, and form reset.
     */
    function initAddFoodModal() {
      const addModal = $id(SELECTORS.addFoodModal);
      const addForm = $id(SELECTORS.addForm);
      const addCancelBtn = $id(SELECTORS.cancelAddBtn);
      const addButtons = document.querySelectorAll(SELECTORS.addFoodBtn);
  
      if (!addButtons || addButtons.length === 0) return;
  
      addButtons.forEach((btn) => {
        if (!btn) return;
        const openHandler = (e) => {
          e.stopPropagation();
          if (addForm) addForm.reset();
          toggleModal(addModal, true);
        };
        btn.addEventListener('click', openHandler);
  
        // keyboard support
        btn.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openHandler(e);
          }
        });
      });
  
      if (addCancelBtn) {
        addCancelBtn.addEventListener('click', () => toggleModal(addModal, false));
        addCancelBtn.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleModal(addModal, false);
          }
        });
      }
    }
  
    /**
     * Parse a numeric dataset value, returning empty string if invalid.
     * @param {string|undefined} value
     * @returns {string}
     */
    function parseDatasetNumber(value) {
      if (value == null) return '';
      const num = Number(value);
      return Number.isFinite(num) ? String(num) : '';
    }
  
    /**
     * Initialize Edit Food modal using event delegation where possible.
     */
    function initEditFoodModal() {
      const editModal = $id(SELECTORS.editFoodModal);
      const editForm = $id(SELECTORS.editForm);
      const cancelEditBtn = $id(SELECTORS.cancelEditBtn);
  
      // Prefer delegation from a container if available to avoid many listeners
      const foodListContainer = document.querySelector('.food-list') || document.body;
  
      if (!foodListContainer) return;
  
      const onFoodItemActivate = (evt) => {
        // Find the clicked .food-item (or its ancestor)
        const el = evt.target.closest && evt.target.closest(SELECTORS.foodItem);
        if (!el) return;
  
        // Populate form and show modal
        if (!editForm || !editModal) return;
  
        toggleModal(editModal, true);
  
        // Safely set form values, guarding for missing inputs
        const setValue = (name, value) => {
          const field = editForm.querySelector(`[name="${name}"]`);
          if (field) field.value = value;
        };
  
        setValue('food_id', el.dataset.id || '');
        setValue('name', el.dataset.name || '');
        setValue('calories', parseDatasetNumber(el.dataset.calories));
        setValue('protein', parseDatasetNumber(el.dataset.protein));
        setValue('carbs', parseDatasetNumber(el.dataset.carbs));
        setValue('fat', parseDatasetNumber(el.dataset.fat));
      };
  
      // Attach both click and keydown (Enter/Space) to support keyboard activation
      foodListContainer.addEventListener('click', onFoodItemActivate);
      foodListContainer.addEventListener('keydown', (e) => {
        if (e.key !== 'Enter' && e.key !== ' ') return;
        onFoodItemActivate(e);
      });
  
      if (cancelEditBtn) {
        cancelEditBtn.addEventListener('click', () => toggleModal(editModal, false));
        cancelEditBtn.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleModal(editModal, false);
          }
        });
      }
    }
  
    // Initialize once DOM is ready
    document.addEventListener('DOMContentLoaded', () => {
      initCollapsibleSections();
      initAddFoodModal();
      initEditFoodModal();
    });
  })();