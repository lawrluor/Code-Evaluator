function displayLogoutConfirmation(phrase) {
	var decision = confirm(phrase);
	if (decision) {
		window.location = "/logout";
	}
}

function deleteAlert(id) {
	var confirmDelete = confirm('Are you sure you want to delete this evaluation?');
	if (confirmDelete) {
		window.location = `/api/deleteEval/${id}`;
	}
}