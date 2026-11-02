let toastTimer;

function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');

  if (!toastComponent) return;

  toastComponent.classList.remove('border-green-500', 'border-[#b42318]', 'border-[#0a84ff]');
  toastComponent.classList.add('border-l-4');

  if (type === 'success') {
      toastComponent.classList.add('border-green-500');
  } else if (type === 'error') {
      toastComponent.classList.add('border-[#b42318]');
  } else {
      toastComponent.classList.add('border-[#0a84ff]');
  }

  // Perbarui konten teks
  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Batalkan timer sebelumnya jika toast masih tampil
  clearTimeout(toastTimer);

  if (!toastComponent.matches(':popover-open')) {
      toastComponent.showPopover();
      requestAnimationFrame(() => {
        toastComponent.classList.remove('opacity-0', 'translate-y-8', 'pointer-events-none');
        toastComponent.classList.add('opacity-100', 'translate-y-0');
      });
  } else {
      toastComponent.classList.remove('opacity-0', 'translate-y-8', 'pointer-events-none');
      toastComponent.classList.add('opacity-100', 'translate-y-0');
  }

  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
      toastComponent.classList.remove('opacity-100', 'translate-y-0');
      toastComponent.classList.add('opacity-0', 'translate-y-8', 'pointer-events-none');
      toastTimer = setTimeout(() => {
        if (toastComponent.matches(':popover-open')) {
          toastComponent.hidePopover();
        }
      }, 300);
  }, duration);
}