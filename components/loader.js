// components/loader.js

document.addEventListener('DOMContentLoaded', () => {
    // 1. Determine BASE_PATH for GitHub pages or local development
    // If the URL contains '/SNS-Groups/', then we are on GitHub Pages or a subdirectory path.
    const basePath = window.location.pathname.includes('/SNS-Groups') ? '/SNS-Groups' : '';

    // Helper to fetch and inject HTML
    async function loadComponent(componentPath, targetId) {
        const targetElement = document.getElementById(targetId);
        if (!targetElement) return;

        try {
            // Adjust the fetch path based on the base path
            const response = await fetch(`${basePath}${componentPath}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            let htmlHTML = await response.text();

            // Replace all instances of {{BASE_PATH}} with the actual base path
            htmlHTML = htmlHTML.replace(/\{\{BASE_PATH\}\}/g, basePath);

            targetElement.innerHTML = htmlHTML;
        } catch (error) {
            console.error(`Failed to load component ${componentPath}:`, error);
        }
    }

    // 2. Load the Header and Footer
    Promise.all([
        loadComponent('/components/header.html', 'global-header'),
        loadComponent('/components/footer.html', 'global-footer')
    ]).then(() => {
        // Dispatch an event so page-level scripts know the header is loaded
        // This is useful for active link highlighting or re-binding mobile menu clicks if needed.
        window.dispatchEvent(new Event('componentsLoaded'));
    });
});
