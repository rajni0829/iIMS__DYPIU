(function() {
    'use strict'
    const forms = document.querySelectorAll('.requires-validation');
    console.log("aa gaya")
    Array.from(forms)
        .forEach(function(form) {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()