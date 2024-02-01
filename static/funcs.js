function displayLogoutConfirmation(phrase) {
	var decision = confirm(phrase);
	if (decision) {
		window.location = "/logout";
	}
}