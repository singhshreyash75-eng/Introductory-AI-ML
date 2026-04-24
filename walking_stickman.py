import tkinter as tk
import math

# ── Canvas & timing ──────────────────────────────────────────────
WIDTH, HEIGHT = 700, 400
FPS           = 60
FRAME_MS      = 1000 // FPS

# ── Stickman geometry ────────────────────────────────────────────
HEAD_R   = 28
BODY_LEN = 80
ARM_LEN  = 55
FORE_LEN = 45
THIGH_L  = 60
SHIN_L   = 55
SHOE_W   = 20
SHOE_H   = 12

# ── Colours ──────────────────────────────────────────────────────
BG_COLOR     = "#1a1a2e"
GROUND_COLOR = "#16213e"
GRID_COLOR   = "#0f3460"
BODY_COLOR   = "#e0e0e0"
JOINT_COLOR  = "#ffffff"
SHOE_COLOR   = "#e94560"
SHOE_OUTLINE = "#ff6b8a"
SHADOW_COLOR = "#0d0d1a"

FACE_YELLOW  = "#FFD93D"
FACE_SHADOW  = "#F6C90E"
EYE_WHITE    = "#ffffff"
EYE_IRIS     = "#2d2d2d"
EYE_SHINE    = "#ffffff"
CHEEK_COLOR  = "#FF8FAB"
SMILE_COLOR  = "#2d2d2d"


def lerp(a, b, t):
    return a + (b - a) * t


class WalkingStickman:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("🚶 Walking Stickman")
        root.configure(bg=BG_COLOR)
        root.resizable(False, False)

        self.canvas = tk.Canvas(
            root, width=WIDTH, height=HEIGHT,
            bg=BG_COLOR, highlightthickness=0
        )
        self.canvas.pack()

        self.ground_y = HEIGHT - 70
        self.x = WIDTH // 2
        self.speed = 2.2

        self.phase = 0.0
        self.phase_speed = 0.09

        self._draw_background()
        self._animate()

    def _draw_background(self):
        steps = 30
        for i in range(steps):
            t   = i / steps
            r   = int(lerp(0x1a, 0x0f, t))
            g   = int(lerp(0x1a, 0x10, t))
            b   = int(lerp(0x2e, 0x20, t))
            col = f"#{r:02x}{g:02x}{b:02x}"
            y0  = i * HEIGHT // steps
            y1  = (i + 1) * HEIGHT // steps
            self.canvas.create_rectangle(0, y0, WIDTH, y1, fill=col, outline="")

        for x in range(0, WIDTH, 60):
            self.canvas.create_line(x, 0, x, self.ground_y, fill=GRID_COLOR, width=1)
        for y in range(0, self.ground_y, 50):
            self.canvas.create_line(0, y, WIDTH, y, fill=GRID_COLOR, width=1)

        self.canvas.create_rectangle(
            0, self.ground_y, WIDTH, HEIGHT,
            fill=GROUND_COLOR, outline=""
        )
        self.canvas.create_line(
            0, self.ground_y, WIDTH, self.ground_y,
            fill="#e94560", width=2
        )
        self.canvas.create_text(
            WIDTH // 2, 22,
            text="✨  W A L K I N G  S T I C K M A N  ✨",
            fill="#e94560", font=("Courier", 13, "bold")
        )

    def _animate(self):
        self.canvas.delete("stickman")

        p = self.phase

        hip_x = self.x
        hip_y = self.ground_y - THIGH_L - SHIN_L - SHOE_H

        shoulder_x = hip_x
        shoulder_y = hip_y - BODY_LEN

        head_x = shoulder_x
        head_y = shoulder_y - HEAD_R - 4

        swing_amp = 0.45
        leg_phase = math.sin(p)

        r_thigh_ang = math.pi / 2 + swing_amp * leg_phase
        l_thigh_ang = math.pi / 2 - swing_amp * leg_phase

        knee_bend = 0.30
        r_knee_ang = r_thigh_ang - knee_bend * max(0,  math.cos(p))
        l_knee_ang = l_thigh_ang - knee_bend * max(0, -math.cos(p))

        r_knee_x = hip_x + THIGH_L * math.cos(r_thigh_ang)
        r_knee_y = hip_y + THIGH_L * math.sin(r_thigh_ang)
        r_foot_x = r_knee_x + SHIN_L * math.cos(r_knee_ang)
        r_foot_y = r_knee_y + SHIN_L * math.sin(r_knee_ang)

        l_knee_x = hip_x + THIGH_L * math.cos(l_thigh_ang)
        l_knee_y = hip_y + THIGH_L * math.sin(l_thigh_ang)
        l_foot_x = l_knee_x + SHIN_L * math.cos(l_knee_ang)
        l_foot_y = l_knee_y + SHIN_L * math.sin(l_knee_ang)

        arm_amp   = 0.45
        r_arm_ang = math.pi / 2 - arm_amp * leg_phase
        l_arm_ang = math.pi / 2 + arm_amp * leg_phase

        fore_bend  = 0.4
        r_elbow_x  = shoulder_x + ARM_LEN * math.cos(r_arm_ang)
        r_elbow_y  = shoulder_y + ARM_LEN * math.sin(r_arm_ang)
        r_hand_x   = r_elbow_x + FORE_LEN * math.cos(r_arm_ang + fore_bend * math.cos(p))
        r_hand_y   = r_elbow_y + FORE_LEN * math.sin(r_arm_ang + fore_bend * math.cos(p))

        l_elbow_x  = shoulder_x + ARM_LEN * math.cos(l_arm_ang)
        l_elbow_y  = shoulder_y + ARM_LEN * math.sin(l_arm_ang)
        l_hand_x   = l_elbow_x + FORE_LEN * math.cos(l_arm_ang - fore_bend * math.cos(p))
        l_hand_y   = l_elbow_y + FORE_LEN * math.sin(l_arm_ang - fore_bend * math.cos(p))

        bob = 3 * abs(math.sin(p))
        head_y     -= bob
        shoulder_y -= bob
        hip_y      -= bob

        tag = "stickman"

        sx, sy = self.x, self.ground_y + 6
        self.canvas.create_oval(
            sx - 30, sy - 6, sx + 30, sy + 6,
            fill=SHADOW_COLOR, outline="", tags=tag
        )

        self._draw_leg(l_knee_x, l_knee_y - bob, l_foot_x, l_foot_y - bob,
                       hip_x, hip_y, "#aaaaaa", "#888888", tag)

        self._draw_arm(shoulder_x, shoulder_y, l_elbow_x, l_elbow_y - bob,
                       l_hand_x, l_hand_y - bob, "#aaaaaa", tag)

        self.canvas.create_line(
            shoulder_x, shoulder_y, hip_x, hip_y,
            fill=BODY_COLOR, width=5, capstyle=tk.ROUND, tags=tag
        )

        self.canvas.create_oval(
            hip_x - 5, hip_y - 5, hip_x + 5, hip_y + 5,
            fill="#e94560", outline="", tags=tag
        )

        self._draw_leg(r_knee_x, r_knee_y - bob, r_foot_x, r_foot_y - bob,
                       hip_x, hip_y, BODY_COLOR, JOINT_COLOR, tag)

        self._draw_arm(shoulder_x, shoulder_y, r_elbow_x, r_elbow_y - bob,
                       r_hand_x, r_hand_y - bob, BODY_COLOR, tag)

        self._draw_emoji_face(head_x, head_y, HEAD_R, tag)

        self.canvas.create_oval(
            shoulder_x - 5, shoulder_y - 5,
            shoulder_x + 5, shoulder_y + 5,
            fill=JOINT_COLOR, outline="", tags=tag
        )

        self.phase += self.phase_speed
        self.x     += self.speed
        if self.x > WIDTH + HEAD_R + 40:
            self.x = -HEAD_R - 40

        self.root.after(FRAME_MS, self._animate)

    def _draw_leg(self, kx, ky, fx, fy, hx, hy, col, joint_col, tag):
        self.canvas.create_line(hx, hy, kx, ky, fill=col, width=5, capstyle=tk.ROUND, tags=tag)

        self.canvas.create_oval(kx - 4, ky - 4, kx + 4, ky + 4,
                                fill=joint_col, outline="", tags=tag)

        self.canvas.create_line(kx, ky, fx, fy,
                                fill=col, width=4, capstyle=tk.ROUND, tags=tag)

        # 🔺 TRIANGULAR SHOE
        sx, sy = fx, fy
        hw, hh = SHOE_W // 2, SHOE_H

        points = [
            sx - hw, sy + hh,
            sx + hw + 4, sy + hh,
            sx, sy
        ]

        self.canvas.create_polygon(
            points,
            fill=SHOE_COLOR,
            outline=SHOE_OUTLINE,
            width=2,
            tags=tag
        )

        self.canvas.create_line(
            sx - hw + 2, sy + hh - 2,
            sx + hw + 2, sy + hh - 2,
            fill=SHOE_OUTLINE, width=1, tags=tag
        )

    def _draw_arm(self, sx, sy, ex, ey, hx, hy, col, tag):
        self.canvas.create_line(sx, sy, ex, ey,
                                fill=col, width=4, capstyle=tk.ROUND, tags=tag)

        self.canvas.create_oval(ex - 3, ey - 3, ex + 3, ey + 3,
                                fill=col, outline="", tags=tag)

        self.canvas.create_line(ex, ey, hx, hy,
                                fill=col, width=3, capstyle=tk.ROUND, tags=tag)

        self.canvas.create_oval(hx - 4, hy - 4, hx + 4, hy + 4,
                                fill=col, outline="", tags=tag)

    def _draw_emoji_face(self, cx, cy, r, tag):
        self.canvas.create_oval(cx - r + 2, cy - r + 4,
                                cx + r + 2, cy + r + 4,
                                fill="#0a0a1a", outline="", tags=tag)

        self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                                fill=FACE_YELLOW, outline=FACE_SHADOW, width=2, tags=tag)

        eye_y   = cy - r * 0.18
        eye_off = r * 0.35
        eye_r   = r * 0.22

        for ex in [cx - eye_off, cx + eye_off]:
            self.canvas.create_oval(ex - eye_r, eye_y - eye_r,
                                    ex + eye_r, eye_y + eye_r,
                                    fill=EYE_WHITE, outline="#ccc", tags=tag)

            ir = eye_r * 0.65
            self.canvas.create_oval(ex - ir, eye_y - ir,
                                    ex + ir, eye_y + ir,
                                    fill=EYE_IRIS, outline="", tags=tag)

        self.canvas.create_arc(cx - r * 0.4, cy + r * 0.1,
                               cx + r * 0.4, cy + r * 0.6,
                               start=200, extent=140,
                               style=tk.ARC, outline=SMILE_COLOR, width=3, tags=tag)


def main():
    root = tk.Tk()
    WalkingStickman(root)
    root.mainloop()


if __name__ == "__main__":
    main()