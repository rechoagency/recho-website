/**
 * UTM Cookie & Form Population
 * 1. Reads UTM params from the URL and stores them in a cookie
 * 2. Reads the cookie and populates hidden fields in a Formspree form
 */

const UTM_PARAMS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
const COOKIE_NAME = 'utm_data';
const COOKIE_DAYS = 30; // How long to persist the cookie

// --- Cookie Helpers ---

function setCookie(name, value, days) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/; SameSite=Lax`;
}

function getCookie(name) {
  const match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
  return match ? decodeURIComponent(match[1]) : null;
}

// --- Step 1: Capture UTM params from URL and save to cookie ---

function captureUTMs() {
  const params = new URLSearchParams(window.location.search);
  const utmData = {};
  let hasUTM = false;

  UTM_PARAMS.forEach(param => {
    if (params.has(param)) {
      utmData[param] = params.get(param);
      hasUTM = true;
    }
  });

  // Only overwrite the cookie if the current URL actually has UTM params.
  // This preserves the original source even as the user navigates.
  if (hasUTM) {
    setCookie(COOKIE_NAME, JSON.stringify(utmData), COOKIE_DAYS);
    console.log('UTM parameters captured:', utmData);
  }
}

// --- Step 2: Read cookie and populate hidden form fields ---

function populateFormFields() {
  const cookieValue = getCookie(COOKIE_NAME);
  if (!cookieValue) {
    console.log('No UTM cookie found');
    return;
  }

  let utmData;
  try {
    utmData = JSON.parse(cookieValue);
    console.log('UTM data from cookie:', utmData);
  } catch (e) {
    console.warn('UTM cookie could not be parsed:', e);
    return;
  }

  UTM_PARAMS.forEach(param => {
    // Select hidden inputs by their name attribute
    const field = document.querySelector(`input[name="${param}"]`);
    if (field && utmData[param]) {
      field.value = utmData[param];
      console.log(`Populated ${param} with: ${utmData[param]}`);
    }
  });
}

// --- Init ---

captureUTMs();

// Populate fields once the DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', populateFormFields);
} else {
  populateFormFields();
}
