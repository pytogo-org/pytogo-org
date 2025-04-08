function resizeGridItems() {
    const grid = document.querySelector('.gallery-grid');
    const rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
    const rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));

    const items = document.querySelectorAll('.gallery-item');
    items.forEach(item => {
        // Use data-height attribute or calculate based on content
        let rowSpan;
        if (item.getAttribute('data-height')) {
            rowSpan = item.getAttribute('data-height');
        } else {
            const height = item.querySelector('img').getBoundingClientRect().height;
            rowSpan = Math.ceil((height + rowGap) / (rowHeight + rowGap));
        }

        item.style.gridRowEnd = `span ${rowSpan}`;
    });
}

// Initialize gallery
window.onload = resizeGridItems;
window.addEventListener('resize', resizeGridItems);

// Images might load after window.onload
const images = document.querySelectorAll('.gallery-item img');
images.forEach(img => {
    img.addEventListener('load', resizeGridItems);
});

// Toggle collapse functionality
const collapseToggle = document.querySelector('.collapse-toggle');
const galleryGrid = document.querySelector('.gallery-grid');

collapseToggle.addEventListener('click', () => {
    galleryGrid.classList.toggle('collapsed');

    if (galleryGrid.classList.contains('collapsed')) {
        collapseToggle.textContent = 'Expand Gallery';
    } else {
        collapseToggle.textContent = 'Collapse Gallery';
    }
});