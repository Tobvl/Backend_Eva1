/**
 * Script para manejar formularios
 */
console.log("Script cargado");
const formRegistro = document.getElementById('formRegistro');
const formLogin = document.getElementById('formLogin');

// Validar formulario de registro
const validarRegistro = async (e) => {
  // Maneja el formulario de registro
  e.preventDefault();

  // Obtener los valores de los campos
  // campos con id: xInput (ej. usernameInput, passwordInput, etc.)
  
  // Obtener campos:
  // username, email, password, confirmpassword
  const username = document.getElementById('usernameInput')
  const email = document.getElementById('emailInput')
  const password = document.getElementById('passwordInput')
  const confirmpassword = document.getElementById('confirmpasswordInput')
    
  // Validar contraseña (8 carácteres, un número y una mayúscula)
  // Expresión regular : se usa entre / /
  // > Validar largo de la contraseña
  if (password.value.length < 8){
    alert('La contraseña debe tener al menos 8 carácteres')
    password.focus()
    return
  }
  // > Validar que la contraseña contenga al menos un número
  if (!/\d/.test(password.value)){
    alert('La contraseña debe contener al menos un número')
    password.focus()
    return
  }
  // > Validar que la contraseña contenga al menos una mayúscula
  if (!/[A-Z]/.test(password.value)){
    alert('La contraseña debe contener al menos una mayúscula')
    password.focus()
    return
  }
  if (password.value != confirmpassword.value){
    alert('Las contraseñas no coinciden')
    confirmpassword.focus()
    return
  }

  
  // Validar que el usuario y correo no existan en el JSON (base de datos)
  // > Buscar en el JSON (GET a /api/usuarios/) y obtener usuarios = data.usuarios
  const usuarios = await fetch('/api/usuarios/')
    .then(response => response.json())
    .then(data => {
      return data.usuarios[0]
    })
    .catch(error => console.log(error))
  try {

    usuarios.forEach(user => {
      if (user.username == username.value){
        alert('Ese usuario ya se encuentra registrado')
        username.focus()
        throw new Error("Ese usuario ya se encuentra registrado");
      }
      if (user.email == email.value){
        alert('Ese correo electrónico ya se encuentra registrado')
        email.focus()
        throw new Error("Ese correo electrónico ya se encuentra registrado!");
        
      }
    });
  }catch (error){
    console.log(error.message)
    return
  }
  
  console.log(usuarios)
  
  // Enviar formulario (POST a /api/usuarios/)
  formRegistro.submit(
    fetch('/api/usuarios/', {
      method: 'POST',
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
  );
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
