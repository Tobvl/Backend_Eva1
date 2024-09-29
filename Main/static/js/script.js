/**
 * Script para manejar formularios
 */
console.log("Script cargado");
const formRegistro = document.getElementById('formRegistro');
const formLogin = document.getElementById('formLogin');

// Validar formulario de registro
const validarRegistro = (e) => {
  // Maneja el formulario de registro
  e.preventDefault();

  // Obtener los valores de los campos
  // campos con id: xInput (ej. usernameInput, passwordInput, etc.)
  
  // Obtener campos:
  // username, email, password, confirmpassword
  const username = document.getElementById('usernameInput').value
  const email = document.getElementById('emailInput').value
  const password = document.getElementById('passwordInput').value
  const confirmpassword = document.getElementById('confirmpasswordInput').value
  
  // Validar que el usuario y correo no existan en el JSON (base de datos)
  // > Buscar en el JSON (GET a /api/usuarios/) y obtener usuarios = data.usuarios
  const usuarios = fetch('/api/usuarios/')
    
  // Validar contraseña (8 carácteres, un número y una mayúscula)
  // Expresión regular : se usa entre / /
  // > Validar largo de la contraseña
  if (password.length < 8){
    alert('La contraseña debe tener al menos 8 carácteres')
    return
  }
  // > Validar que la contraseña contenga al menos un número
  if (!/\d/.test(password)){
    alert('La contraseña debe contener al menos un número')
    return
  }
  // > Validar que la contraseña contenga al menos una mayúscula
  if (!/[A-Z]/.test(password)){
    alert('La contraseña debe contener al menos una mayúscula')
    return
  }
  formRegistro.submit();
}

const validarLogin = () => {
  // Maneja el formulario de login
}

if (formRegistro != null){
  console.log("Formulario de registro encontrado");
  // Agregar validarRegistro al evento onsubmit del formulario
  formRegistro.addEventListener('submit', validarRegistro);

}

if (formLogin != null){
  console.log("Formulario de login encontrado");
  formLogin.onsubmit = validarLogin;
}
