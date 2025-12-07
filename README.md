# Meme Generator – Docker projekt

Enostaven spletni **Meme Generator**, napisan v Pythonu z **Flaskom** in zapakiran v **Docker**.

## Kaj zna

- Naložiš sliko preko obrazca v brskalniku.  
- Dodaš zgornji in spodnji tekst (klasičen meme stil).  
- Pillow ustvari novo sliko s tekstom.  
- Meme se ti prikaže kar v brskalniku.

## Tehnologije

- Python 3.12  
- Flask  
- Pillow  
- Docker

## Kako pognati z Dockerjem

```bash
docker build -t meme-generator .
docker run -p 5000:5000 meme-generator
