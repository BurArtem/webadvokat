const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  console.log('--- Checking Desktop Version (1920x1080) ---');
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('http://localhost:8000/index.html');
  
  // Check Photo Visibility
  const photoVisible = await page.isVisible('.hero-main-photo');
  console.log(`Desktop Photo Visible: ${photoVisible}`);

  // Check Background Image
  const bgImage = await page.evaluate(() => {
    const el = document.querySelector('.first_section');
    return window.getComputedStyle(el).backgroundImage;
  });
  console.log(`Desktop Background: ${bgImage}`); // Should contain Work.jpg

  // Check Parallax
  const initialTransform = await page.evaluate(() => {
    const el = document.querySelector('.hero-main-photo');
    return window.getComputedStyle(el).transform;
  });
  console.log(`Initial Transform: ${initialTransform}`);

  await page.evaluate(() => window.scrollBy(0, 500));
  await page.waitForTimeout(1000); // Wait for scroll event to fire

  const scrolledTransform = await page.evaluate(() => {
    const el = document.querySelector('.hero-main-photo');
    return window.getComputedStyle(el).transform;
  });
  console.log(`Scrolled Transform (after 500px): ${scrolledTransform}`);

  if (initialTransform !== scrolledTransform) {
      console.log('Parallax Effect: WORKING');
  } else {
      console.log('Parallax Effect: NOT WORKING');
  }

  console.log('\n--- Checking Mobile Version (375x812) ---');
  await page.setViewportSize({ width: 375, height: 812 });
  await page.reload();

  // Check Photo Visibility (Should be hidden)
  const mobilePhotoVisible = await page.isVisible('.hero-main-photo');
  console.log(`Mobile Photo Visible (should be false): ${mobilePhotoVisible}`);

  // Check Background Image
  const mobileBgImage = await page.evaluate(() => {
    const el = document.querySelector('.first_section');
    return window.getComputedStyle(el).backgroundImage;
  });
  console.log(`Mobile Background: ${mobileBgImage}`); // Should contain Main_photo.png

  // Check Blur Overlay
  const hasBlur = await page.evaluate(() => {
    const el = document.querySelector('.first_section');
    const beforeStyle = window.getComputedStyle(el, '::before');
    return beforeStyle.backdropFilter.includes('blur') || beforeStyle.webkitBackdropFilter.includes('blur');
  });
  console.log(`Mobile Blur Overlay Present: ${hasBlur}`);

  await browser.close();
})();
