chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
  const tab = tabs[0];
  const video_id = tab.url.slice(32, tab.length);
  const summary_display = document.querySelector('#summary')
  const loader = document.querySelector('#loader')

  try {
    const response = await fetch(`https://sumsum-ext-backend.fly.dev/summarize/${video_id}`)
    const summary = await response.json()
    
    summary_display.innerText = summary
    loader.style.display = "none"
  } catch (err) {
    loader.style.display = "none"
    summary_display.innerText = "There was an error generating summary"
  }
});
