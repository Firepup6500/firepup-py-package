echo "🧽 Pruging old package files... 🧽"
rm -rf dist
mkdir dist
echo "🧹 Formatting... 🧹"
black . > /dev/null
echo "🛠  Building... 🛠"
poetry build > /dev/null
echo -n "☁️  Uploading... ☁️"
poetry publish -u __token__ -p $TOKEN
echo "✨ All done! ✨"
