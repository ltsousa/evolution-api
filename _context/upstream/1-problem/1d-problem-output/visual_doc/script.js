// Raffles and Experiences Management - Visual Documentation Script

class VisualDocumentationManager {
  constructor() {
    this.init();
  }

  init() {
    this.setupProgressBar();
    this.setupBackToTop();
    this.setupSmoothScroll();
    this.setupCopyToClipboard();
    this.setupKeyboardShortcuts();
    this.setupRippleEffects();
    this.setupTooltips();
    this.animateOnScroll();
  }

  // Progress Bar
  setupProgressBar() {
    const progressBar = document.createElement('div');
    progressBar.className = 'progress-bar';
    document.body.appendChild(progressBar);

    const updateProgress = () => {
      const scrollTop = window.pageYOffset;
      const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / documentHeight) * 100;
      progressBar.style.width = `${Math.min(progress, 100)}%`;
    };

    window.addEventListener('scroll', updateProgress);
    updateProgress();
  }

  // Back to Top Button
  setupBackToTop() {
    const backToTop = document.createElement('button');
    backToTop.className = 'back-to-top';
    backToTop.innerHTML = '↑';
    backToTop.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTop);

    const toggleVisibility = () => {
      if (window.pageYOffset > 300) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    };

    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });

    window.addEventListener('scroll', toggleVisibility);
  }

  // Smooth Scroll for Navigation
  setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
          const offsetTop = target.offsetTop - 80; // Account for fixed navbar
          window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // Copy to Clipboard for Section Links
  setupCopyToClipboard() {
    // Add copy buttons to headings
    document.querySelectorAll('h2, h3, h4').forEach(heading => {
      const copyButton = document.createElement('button');
      copyButton.className = 'copy-link';
      copyButton.innerHTML = '🔗';
      copyButton.setAttribute('aria-label', 'Copy link to section');
      
      const headingId = heading.id || this.generateId(heading.textContent);
      heading.id = headingId;
      
      copyButton.addEventListener('click', () => {
        const url = `${window.location.origin}${window.location.pathname}#${headingId}`;
        this.copyToClipboard(url, 'Section link copied to clipboard!');
      });
      
      heading.appendChild(copyButton);
    });
  }

  // Keyboard Shortcuts
  setupKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
      // Ctrl+H or Cmd+H - Go to home
      if ((e.ctrlKey || e.metaKey) && e.key === 'h') {
        e.preventDefault();
        window.location.href = 'index.html';
      }
      
      // Ctrl+P or Cmd+P - Print (let browser handle it)
      if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
        // Browser handles this automatically
      }
      
      // Escape - Close any open modals/tooltips
      if (e.key === 'Escape') {
        this.closeTooltips();
      }
    });
  }

  // Ripple Effects for Buttons
  setupRippleEffects() {
    document.querySelectorAll('.btn, .dashboard-card').forEach(element => {
      element.classList.add('ripple');
    });
  }

  // Simple Tooltips
  setupTooltips() {
    document.querySelectorAll('[data-tooltip]').forEach(element => {
      const tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = element.getAttribute('data-tooltip');
      
      element.addEventListener('mouseenter', () => {
        document.body.appendChild(tooltip);
        this.positionTooltip(element, tooltip);
      });
      
      element.addEventListener('mouseleave', () => {
        if (tooltip.parentNode) {
          tooltip.parentNode.removeChild(tooltip);
        }
      });
    });
  }

  // Animate elements on scroll
  animateOnScroll() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in-up');
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    document.querySelectorAll('.card').forEach(card => {
      observer.observe(card);
    });
  }

  // Utility Functions
  generateId(text) {
    return text.toLowerCase()
      .replace(/[^\w\s-]/g, '')
      .replace(/\s+/g, '-')
      .trim();
  }

  async copyToClipboard(text, message = 'Copied to clipboard!') {
    try {
      await navigator.clipboard.writeText(text);
      this.showToast(message, 'success');
    } catch (err) {
      // Fallback for older browsers
      const textArea = document.createElement('textarea');
      textArea.value = text;
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand('copy');
      document.body.removeChild(textArea);
      this.showToast(message, 'success');
    }
  }

  showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
      <div class="toast-content">
        <span>${message}</span>
        <button class="toast-close" onclick="this.parentElement.parentElement.remove()">×</button>
      </div>
    `;
    
    document.body.appendChild(toast);
    
    // Show toast
    setTimeout(() => toast.classList.add('show'), 100);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => {
        if (toast.parentNode) {
          toast.parentNode.removeChild(toast);
        }
      }, 300);
    }, 3000);
  }

  positionTooltip(element, tooltip) {
    const rect = element.getBoundingClientRect();
    tooltip.style.position = 'absolute';
    tooltip.style.background = '#333';
    tooltip.style.color = 'white';
    tooltip.style.padding = '8px 12px';
    tooltip.style.borderRadius = '4px';
    tooltip.style.fontSize = '14px';
    tooltip.style.zIndex = '9999';
    tooltip.style.top = `${rect.top - 40}px`;
    tooltip.style.left = `${rect.left + (rect.width / 2)}px`;
    tooltip.style.transform = 'translateX(-50%)';
  }

  closeTooltips() {
    document.querySelectorAll('.tooltip').forEach(tooltip => {
      if (tooltip.parentNode) {
        tooltip.parentNode.removeChild(tooltip);
      }
    });
  }
}

// Dashboard specific functionality
class DashboardManager extends VisualDocumentationManager {
  constructor() {
    super();
    this.setupDashboard();
  }

  setupDashboard() {
    this.loadReportMetrics();
    this.setupQuickNavigation();
  }

  loadReportMetrics() {
    // This would typically load from API or local storage
    const metrics = {
      totalIssues: 12,
      criticalIssues: 3,
      processStages: 14,
      automationPotential: '95%'
    };

    // Update dashboard metrics if elements exist
    Object.entries(metrics).forEach(([key, value]) => {
      const element = document.querySelector(`[data-metric="${key}"]`);
      if (element) {
        element.textContent = value;
      }
    });
  }

  setupQuickNavigation() {
    document.querySelectorAll('.dashboard-card').forEach(card => {
      card.addEventListener('click', () => {
        const link = card.querySelector('a');
        if (link) {
          window.location.href = link.href;
        }
      });
    });
  }
}

// Table enhancement
class TableManager {
  constructor() {
    this.enhanceTables();
  }

  enhanceTables() {
    document.querySelectorAll('table').forEach(table => {
      this.makeSortable(table);
      this.addMobileResponsiveness(table);
    });
  }

  makeSortable(table) {
    const headers = table.querySelectorAll('thead th');
    headers.forEach((header, index) => {
      header.style.cursor = 'pointer';
      header.addEventListener('click', () => this.sortTable(table, index));
    });
  }

  sortTable(table, columnIndex) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    const isNumeric = this.isNumericColumn(rows, columnIndex);
    
    rows.sort((a, b) => {
      const aValue = a.children[columnIndex].textContent.trim();
      const bValue = b.children[columnIndex].textContent.trim();
      
      if (isNumeric) {
        return parseFloat(aValue) - parseFloat(bValue);
      } else {
        return aValue.localeCompare(bValue);
      }
    });
    
    rows.forEach(row => tbody.appendChild(row));
  }

  isNumericColumn(rows, columnIndex) {
    const sample = rows.slice(0, 3);
    return sample.every(row => {
      const value = row.children[columnIndex].textContent.trim();
      return !isNaN(parseFloat(value)) && isFinite(value);
    });
  }

  addMobileResponsiveness(table) {
    const wrapper = document.createElement('div');
    wrapper.className = 'table-container';
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  }
}

// Initialize based on page type
document.addEventListener('DOMContentLoaded', () => {
  if (document.body.classList.contains('dashboard')) {
    new DashboardManager();
  } else {
    new VisualDocumentationManager();
  }
  
  new TableManager();
  
  // Add loading state removal
  document.body.classList.remove('loading');
});

// Service Worker for offline capability (optional)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('SW registered: ', registration);
      })
      .catch(registrationError => {
        console.log('SW registration failed: ', registrationError);
      });
  });
}

// Print functionality
window.addEventListener('beforeprint', () => {
  document.body.classList.add('printing');
});

window.addEventListener('afterprint', () => {
  document.body.classList.remove('printing');
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { VisualDocumentationManager, DashboardManager, TableManager };
} 