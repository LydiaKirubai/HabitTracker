document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('li form button');

  buttons.forEach(button => {
    button.addEventListener('click', async (e) => {
      e.preventDefault();
      const form = button.closest('form');
      const action = form.action;

      // Send POST request using fetch
      const response = await fetch(action, { method: 'POST' });
      if (response.ok) {
        // Reload page or update UI
        location.reload();
      } else {
        alert('Error toggling habit.');
      }
    });
  });
});
