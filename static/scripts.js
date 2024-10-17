function checkDuplicateUserId() {
    const userId = document.getElementById('user_id').value;
    fetch('/check_user_id', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: userId })
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('user_id_check_result');
        resultElement.textContent = data.message;
        if (data.status === 'success') {
            resultElement.className = 'success';
        } else {
            resultElement.className = 'fail';
        }
    });
}

function checkPasswordMatch() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const resultElement = document.getElementById('password_check_result');
    if (password === confirmPassword) {
        resultElement.textContent = '입력한 비밀번호와 동일합니다.';
        resultElement.className = 'success';
    } else {
        resultElement.textContent = '입력한 비밀번호가 다릅니다.';
        resultElement.className = 'fail';
    }
}
