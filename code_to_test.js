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