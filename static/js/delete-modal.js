document.addEventListener('click', (event) => {
  const closeButton = event.target.closest('[data-dialog-close]');
  if (closeButton) {
    closeButton.closest('dialog')?.close();
    return;
  }

  const deleteButton = event.target.closest('[data-delete-url]');
  if (!deleteButton) return;

  const template = document.getElementById('delete-confirmation-template');
  if (!template) return;

  const dialog = template.content.firstElementChild.cloneNode(true);
  const form = dialog.querySelector('form');
  form.action = deleteButton.dataset.deleteUrl;
  document.body.append(dialog);
  dialog.addEventListener('click', (dialogEvent) => {
    if (dialogEvent.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => dialog.remove(), { once: true });
  dialog.showModal();
});
