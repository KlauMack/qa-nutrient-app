// daily_summary.js

// Collapse sections
document.querySelectorAll('.food-section-content').forEach(content => {
    if (content.children.length === 0) {
      content.style.maxHeight = '0px';
    } else {
      content.style.maxHeight = content.scrollHeight + 'px';
    }
  });
  
  document.querySelectorAll('.food-section-toggle').forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      const chevron = header.querySelector('.chevron-icon');
      chevron.classList.toggle('rotate-180');
      if (content.style.maxHeight && content.style.maxHeight !== '0px') {
        content.style.maxHeight = '0px';
      } else {
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });
  
  // Add food modal
  const addModal = document.getElementById('food-entry-modal');
  const addButtons = document.querySelectorAll('.add-food-btn');
  const addCancelBtn = document.getElementById('cancel-food-btn');
  const addForm = document.getElementById('food-entry-form');
  
  addButtons.forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      addForm.reset();
      addModal.classList.remove('hidden');
    });
  });
  
  addCancelBtn.addEventListener('click', () => {
    addModal.classList.add('hidden');
  });
  
  // Edit food modal
  document.querySelectorAll('.food-item').forEach(item => {
    item.addEventListener('click', () => {
      const editModal = document.getElementById('food-edit-modal');
      const editForm = document.getElementById('food-edit-form');
  
      editModal.classList.remove('hidden');
      editForm.querySelector('[name="food_id"]').value = item.dataset.id;
      editForm.querySelector('[name="name"]').value = item.dataset.name;
      editForm.querySelector('[name="calories"]').value = item.dataset.calories;
      editForm.querySelector('[name="protein"]').value = item.dataset.protein;
      editForm.querySelector('[name="carbs"]').value = item.dataset.carbs;
      editForm.querySelector('[name="fat"]').value = item.dataset.fat;
    });
  });
  
  document.getElementById('cancel-edit-btn').addEventListener('click', () => {
    document.getElementById('food-edit-modal').classList.add('hidden');
  });
  