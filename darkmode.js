/*
Configuración de Tailwind desde el navegador:
- darkMode: 'class' indica que las variantes "dark:*" se activan cuando un ancestro
  (habitualmente <html>) tiene la clase "dark". Esto permite alternar tema con JS
  simplemente añadiendo/quitando esa clase.
*/
tailwind.config = {
  darkMode: 'class'
};

/*
  Script para alternar el modo oscuro:
  - document.documentElement => referencia al <html>.
  - classList.toggle('dark') => agrega/quita la clase "dark".
  - Gracias a tailwind.config.darkMode='class', todas las utilidades "dark:*"
    se activan o desactivan inmediatamente (con transición por "transition-colors").
*/
function toggleDarkMode() {
  document.documentElement.classList.toggle('dark');
};