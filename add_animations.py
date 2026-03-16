import os

file_path = r'c:\Users\kazum\.gemini\antigravity\scratch\ensure-next-lp\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add scripts to the Head
script_tags = """    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js"></script>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>"""
content = content.replace("""    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>""", script_tags)

# 2. Add CSS
css_addition = """        .delay-500 { animation-delay: 500ms; }
        
        /* Reveal on Scroll */
        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: opacity, transform;
        }
        .reveal-on-scroll.is-visible {
            opacity: 1;
            transform: translateY(0);
        }
        
        /* Ensure tilt elements look crisp */
        .js-tilt-glare {
            border-radius: inherit;
        }"""
content = content.replace("        .delay-500 { animation-delay: 500ms; }", css_addition)

# 3. Add particles to hero
hero_bg = """        <!-- Background Image with Overlay -->
        <div class="absolute inset-0 z-0 overflow-hidden bg-slate-100">
            <img src="./office_people_working.png" alt="Office working" class="w-full h-full object-cover object-center opacity-90 animate-subtle-zoom">
            <div class="absolute inset-0 bg-gradient-to-r from-white via-white/80 to-transparent z-10"></div>
            <div id="particles-js" class="absolute inset-0 mix-blend-screen opacity-50 z-20"></div>
        </div>"""
content = content.replace("""        <!-- Background Image with Overlay -->
        <div class="absolute inset-0 z-0 overflow-hidden bg-slate-100">
            <img src="./office_people_working.png" alt="Office working" class="w-full h-full object-cover object-center opacity-90 animate-subtle-zoom">
            <div class="absolute inset-0 bg-gradient-to-r from-white via-white/80 to-transparent"></div>
        </div>""", hero_bg)

# 4. Add reveal-on-scroll classes to multiple elements
content = content.replace('class="grid md:grid-cols-3 gap-12"', 'class="grid md:grid-cols-3 gap-12 reveal-on-scroll"')
content = content.replace('class="text-center mb-16"', 'class="text-center mb-16 reveal-on-scroll"')
content = content.replace('class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5"', 'class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 reveal-on-scroll"')
content = content.replace('class="grid lg:grid-cols-3 gap-8 items-start"', 'class="grid lg:grid-cols-3 gap-8 items-start reveal-on-scroll"')
content = content.replace('class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-12 gap-6"', 'class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-12 gap-6 reveal-on-scroll"')
content = content.replace('class="grid md:grid-cols-3 gap-8"', 'class="grid md:grid-cols-3 gap-8 reveal-on-scroll"')
content = content.replace('class="bg-white rounded-2xl p-8 md:p-12 border border-slate-200 shadow-xl shadow-slate-200/50"', 'class="bg-white rounded-2xl p-8 md:p-12 border border-slate-200 shadow-xl shadow-slate-200/50 reveal-on-scroll"')

# 5. Add data-tilt attributes and remove vertical transform on hover to prevent conflicts
content = content.replace('class="p-6 bg-white border border-slate-200 rounded-xl flex items-center gap-4 hover:border-blue-400 hover:shadow-lg hover:-translate-y-1 transition-all group"', 'class="p-6 bg-white border border-slate-200 rounded-xl flex items-center gap-4 hover:border-blue-400 transition-shadow duration-300 group" data-tilt data-tilt-max="10" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2"')
content = content.replace('class="border border-slate-200 rounded-2xl p-8 hover:shadow-xl transition-shadow bg-slate-50"', 'class="border border-slate-200 rounded-2xl p-8 hover:shadow-xl transition-shadow duration-300 bg-slate-50" data-tilt data-tilt-max="5" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.1"')
content = content.replace('class="border-2 border-blue-600 rounded-2xl p-8 shadow-2xl bg-white relative lg:-translate-y-4"', 'class="border-2 border-blue-600 rounded-2xl p-8 shadow-2xl bg-white relative lg:-translate-y-4 transition-shadow duration-300" data-tilt data-tilt-max="5" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2"')
content = content.replace('class="border border-slate-200 rounded-2xl p-8 hover:shadow-xl transition-shadow bg-white"', 'class="border border-slate-200 rounded-2xl p-8 hover:shadow-xl transition-shadow duration-300 bg-white" data-tilt data-tilt-max="5" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.1"')
content = content.replace('class="group flex flex-col bg-white border border-slate-200 rounded-2xl overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all"', 'class="group flex flex-col bg-white border border-slate-200 rounded-2xl overflow-hidden hover:shadow-xl transition-shadow duration-300" data-tilt data-tilt-max="5" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2"')

# 6. Add JS logic
js_addition = """// Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                    // Close mobile menu if open
                    mobileMenu.classList.add('hidden');
                }
            });
        });

        // Intersection Observer for Reveal on Scroll
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.15
        };
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.reveal-on-scroll').forEach(element => {
            observer.observe(element);
        });

        // Particles.js initialized for subtle hero background
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', {
                "particles": {
                    "number": {
                        "value": 50,
                        "density": { "enable": true, "value_area": 800 }
                    },
                    "color": { "value": "#2563eb" },
                    "shape": { "type": "circle" },
                    "opacity": {
                        "value": 0.5,
                        "random": true,
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#3b82f6",
                        "opacity": 0.4,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 1.5,
                        "direction": "none",
                        "random": true,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": { "enable": true, "mode": "grab" },
                        "onclick": { "enable": false },
                        "resize": true
                    },
                    "modes": {
                        "grab": { "distance": 180, "line_linked": { "opacity": 0.6 } }
                    }
                },
                "retina_detect": true
            });
        }"""
content = content.replace("""// Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                    // Close mobile menu if open
                    mobileMenu.classList.add('hidden');
                }
            });
        });""", js_addition)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied animations to index.html")
