let activeConfirmation;

window.confirmDelete = function() {
  if (activeConfirmation) return activeConfirmation;
  const template = document.getElementById('delete-confirmation-template');
  if (!template) throw new Error('Delete confirmation template is missing.');

  const dialog = template.content.firstElementChild.cloneNode(true);
  const form = dialog.querySelector('form');
  document.body.append(dialog);

  activeConfirmation = new Promise((resolve) => {
    let resolved = false;
    const finish = (confirmed) => {
      if (resolved) return;
      resolved = true;
      dialog.removeEventListener('close', handleClose);
      if (dialog.open) dialog.close();
      dialog.remove();
      activeConfirmation = null;
      resolve(confirmed);
    };
    const handleClose = () => finish(false);

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      finish(true);
    });
    dialog.addEventListener('click', (event) => {
      const closeButton = event.target.closest('[data-dialog-close]');
      if (closeButton || event.target === dialog) finish(false);
    });
    dialog.addEventListener('close', handleClose);
    dialog.showModal();
  });

  return activeConfirmation;
};

document.addEventListener('click', (event) => {
  const closeButton = event.target.closest('[data-dialog-close]');
  if (closeButton) {
    closeButton.closest('dialog')?.close();
    return;
  }

  const deleteButton = event.target.closest('[data-delete-url]');
  if (!deleteButton) return;

  const template = document.getElementById('delete-confirmation-template');
  if (!template) throw new Error('Delete confirmation template is missing.');

  const dialog = template.content.firstElementChild.cloneNode(true);
  dialog.querySelector('form').action = deleteButton.dataset.deleteUrl;
  document.body.append(dialog);
  dialog.addEventListener('click', (dialogEvent) => {
    if (dialogEvent.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => dialog.remove(), { once: true });
  dialog.showModal();
});
