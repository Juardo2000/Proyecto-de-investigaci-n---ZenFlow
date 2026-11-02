// static/js/main.js - Lógica de validaciones para el registro en ZenFlow

document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    
    if (registerForm) {
        const pass1 = document.getElementById('reg_password');
        const pass2 = document.getElementById('reg_confirm_password');
        const cedulaInput = document.getElementById('reg_cedula');
        const telefonoInput = document.getElementById('reg_telefono');
        const correoInput = document.getElementById('reg_correo');

        registerForm.addEventListener('submit', function(e) {
            // 1. Validar que las contraseñas coincidan
            if (pass1.value !== pass2.value) {
                e.preventDefault();
                alert('❌ Las contraseñas no coinciden. Por favor, revísalas.');
                pass2.focus();
                return;
            }

            // 2. Validar formato de Cédula (Ej: números solos o con V-/E- opcional, 6 a 9 dígitos)
            const cedulaRegex = /^[VEve]?[-]?\d{6,9}$/;
            if (!cedulaRegex.test(cedulaInput.value.trim())) {
                e.preventDefault();
                alert('❌ Formato de cédula inválido. Ingrese solo números o prefijo V/E (Ej: 12345678).');
                cedulaInput.focus();
                return;
            }

            // 3. Validar formato de Teléfono (Ej: 10 a 11 dígitos, formato venezolano común como 0414...)
            const telefonoRegex = /^0(2|4)\d{9}$/;
            if (!telefonoRegex.test(telefonoInput.value.trim())) {
                e.preventDefault();
                alert('❌ Formato de teléfono inválido. Debe iniciar con 0 (Ej: 04141234567).');
                telefonoInput.focus();
                return;
            }

            // 4. Validar formato básico de Correo Electrónico
            const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!correoRegex.test(correoInput.value.trim())) {
                e.preventDefault();
                alert('❌ El formato del correo electrónico no es válido.');
                correoInput.focus();
                return;
            }

            // Simulación visual del botón de envío con verificación por correo
            const submitBtn = document.getElementById('btnSubmitRegister');
            submitBtn.value = "Enviando correo de verificación...";
            submitBtn.style.opacity = "0.7";
        });
    }
});