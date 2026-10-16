from playwright.sync_api import Page, expect

def test_form_shows_submitted_value(page: Page):
    page.set_content("<input id='name'><button>Salvar</button><p id='result'></p><script>document.querySelector('button').onclick=()=>document.querySelector('#result').textContent=document.querySelector('#name').value</script>")
    page.locator("#name").fill("Luiz Henrique")
    page.get_by_role("button", name="Salvar").click()
    expect(page.locator("#result")).to_have_text("Luiz Henrique")
