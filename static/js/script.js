function setFocus(on) {
    var element = document.activeElement;
    if (on) {
        setTimeout(function () {
            element.parentNode.classList.add("focus");
        });
    } else {
        let box = document.querySelector(".input-box");
        box.classList.remove("focus");
        $("input").each(function () {
            var $input = $(this);
            var $parent = $input.closest(".input-box");
            if ($input.val()) $parent.addClass("focus");
            else $parent.removeClass("focus");
        });
    }
}


function validateForm() {
    var link = document.forms["form"]["link"].value;
    var phone = document.forms["form"]["phone"].value;

    if (!link.startsWith("https://www.myauto.ge/")) {
        alert("Link must start with https://www.myauto.ge/");
        return false;
    }

    if (!phone.startsWith("5") || phone.length < 9 || phone.length > 9) {
        alert("Phone number must start with 5 and be exactly 9 characters long");
        return false;
    }

    return true;
}

var countdownIntervalId; // Global variable to store the interval ID for countdown timer

    function validatePhone() {
        var phoneInput = document.getElementById('phone');
        var sendButton = document.getElementById('send-sms-code');
        var phoneValue = phoneInput.value;

        // Use a regular expression to check if the phone number is in the correct format
        var phoneRegex = /^5\d{8}$/;
        var isValidPhone = phoneRegex.test(phoneValue);

        // Enable/disable the send button based on phone number format
        sendButton.disabled = !isValidPhone;
    }

    function sendSmsCode() {
        var phone = document.getElementById('phone').value;
        var sendButton = document.getElementById('send-sms-code');

        // Disable the send button for 1 minute (60 seconds)
        sendButton.disabled = true;
        countdown(60);

        // Create an HTTP request object
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/send_sms_code', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

        xhr.onload = function() {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
            } else {
                console.error('Error:', xhr.statusText);
            }
        };
        xhr.onerror = function() {
            console.error('Network Error');
        };

        xhr.send(JSON.stringify({phone: phone}));
    }

    function countdown(seconds) {
        var sendButton = document.getElementById('send-sms-code');
        var intervalId = setInterval(function() {
            seconds--;
            sendButton.textContent = 'Resend in ' + seconds + 's';
            if (seconds <= 0) {
                clearInterval(intervalId);
                sendButton.textContent = 'send';
                sendButton.disabled = false;
            }
        }, 1000);
    }