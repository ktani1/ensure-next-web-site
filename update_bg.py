import os
import re

file_path = r'c:\Users\kazum\.gemini\antigravity\scratch\ensure-next-lp\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove particles.js script
content = content.replace('    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>\n', '')

# 2. Replace particles div with canvas
old_hero_bg = """        <!-- Background Image with Overlay -->
        <div class="absolute inset-0 z-0 overflow-hidden bg-slate-100">
            <img src="./office_people_working.png" alt="Office working" class="w-full h-full object-cover object-center opacity-90 animate-subtle-zoom">
            <div class="absolute inset-0 bg-gradient-to-r from-white via-white/80 to-transparent z-10"></div>
            <div id="particles-js" class="absolute inset-0 mix-blend-screen opacity-50 z-20"></div>
        </div>"""

new_hero_bg = """        <!-- Background Image with Overlay -->
        <div class="absolute inset-0 z-0 overflow-hidden bg-slate-100">
            <img src="./office_people_working.png" alt="Office working" class="w-full h-full object-cover object-center opacity-90 animate-subtle-zoom">
            <div class="absolute inset-0 bg-gradient-to-r from-white via-white/90 to-white/20 z-10 pointer-events-none"></div>
            <canvas id="tech-canvas" class="absolute inset-0 w-full h-full z-20 mix-blend-multiply opacity-80 pointer-events-none"></canvas>
        </div>"""
content = content.replace(old_hero_bg, new_hero_bg)

# 3. Replace Particles.js JS logic with custom 3D rotating network logic
old_js = """        // --- 2. Particles.js (Hero Background) ---
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', {
                "particles": {
                    "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": "#2563eb" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.4, "random": true },
                    "size": { "value": 3, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": "#3b82f6", "opacity": 0.4, "width": 1 },
                    "move": { "enable": true, "speed": 1.5, "direction": "none", "random": true, "out_mode": "out" }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": false }, "resize": true },
                    "modes": { "grab": { "distance": 180, "line_linked": { "opacity": 0.6 } } }
                },
                "retina_detect": true
            });
        }"""

new_js = """        // --- 2. Custom 3D Tech Network Animation (Hero Background) ---
        const canvas = document.getElementById('tech-canvas');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            let width, height;
            let nodes = [];
            const numNodes = 120;

            function resize() {
                width = canvas.width = window.innerWidth;
                height = canvas.height = canvas.parentElement.offsetHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            class Node {
                constructor() {
                    // Random positions sphere (-1 to 1)
                    this.x = (Math.random() - 0.5) * 2;
                    this.y = (Math.random() - 0.5) * 2;
                    this.z = (Math.random() - 0.5) * 2;
                    this.origX = this.x;
                    this.origZ = this.z;
                    // Different rotation speeds for complexity
                    this.speed = (Math.random() * 0.0015) + 0.0005;
                    this.speed *= Math.random() < 0.5 ? 1 : -1;
                    this.angle = Math.random() * Math.PI * 2;
                }
                update() {
                    this.angle += this.speed;
                    // Rotate around Y axis
                    this.x = this.origX * Math.cos(this.angle) - this.origZ * Math.sin(this.angle);
                    this.z = this.origZ * Math.cos(this.angle) + this.origX * Math.sin(this.angle);
                    // Slow rotation around X axis for full 3D feel
                    this.y += Math.sin(this.angle * 0.5) * 0.001; 
                }
            }

            for(let i=0; i<numNodes; i++) nodes.push(new Node());

            function draw() {
                ctx.clearRect(0, 0, width, height);
                // Perspective magic
                const perspective = width * 0.8; 
                const centerX = width / 2;
                const centerY = height / 2;
                
                // Project 3D to 2D
                const projected = nodes.map(n => {
                    n.update();
                    const z = n.z + 1.5; // Offset camera distance
                    const scale = perspective / (perspective + z * 400); // Scale by distance
                    return {
                        x: centerX + n.x * 600 * scale,
                        y: centerY + n.y * 400 * scale,
                        scale: scale,
                        z: z
                    };
                });

                // Sort by Z index to draw back-to-front (though additive blending doesn't care much)
                projected.sort((a, b) => b.z - a.z);

                // Draw connecting lines (network)
                ctx.lineWidth = 1;
                for(let i=0; i<projected.length; i++) {
                    for(let j=i+1; j<projected.length; j++) {
                        const dx = projected[i].x - projected[j].x;
                        const dy = projected[i].y - projected[j].y;
                        const distSq = dx*dx + dy*dy;
                        
                        // Only draw lines if close enough
                        if(distSq < 15000) {
                            // Fade based on distance and depth
                            const opacity = Math.max(0, 1 - distSq / 15000) * (1 / projected[i].z) * 0.4;
                            ctx.strokeStyle = `rgba(37, 99, 235, ${opacity})`; // blue-600
                            ctx.beginPath();
                            ctx.moveTo(projected[i].x, projected[i].y);
                            ctx.lineTo(projected[j].x, projected[j].y);
                            ctx.stroke();
                        }
                    }
                }

                // Draw nodes (dots)
                projected.forEach(p => {
                    const dotOpacity = Math.max(0.1, (1 / p.z) * 0.8);
                    ctx.fillStyle = `rgba(37, 99, 235, ${dotOpacity})`;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, Math.max(0.5, p.scale * 2.5), 0, Math.PI*2);
                    ctx.fill();
                });

                requestAnimationFrame(draw);
            }
            draw();
        }"""
content = content.replace(old_js, new_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully replaced particles with custom 3D tech network animation.")
