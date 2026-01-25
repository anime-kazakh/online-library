document.querySelector('textarea').addEventListener('keydown', function(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    e.target.form.requestSubmit();
  }
});
