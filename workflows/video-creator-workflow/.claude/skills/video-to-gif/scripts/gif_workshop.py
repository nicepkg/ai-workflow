#!/usr/bin/env python3
"""
Video to GIF Workshop - Convert videos to optimized GIFs
Features: clipping, speed control, text overlays, and smart optimization.
"""

import io
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np
from PIL import Image, ImageDraw, ImageFont

try:
    from moviepy.editor import (
        ColorClip,
        CompositeVideoClip,
        TextClip,
        VideoFileClip,
        concatenate_videoclips,
        vfx,
    )
    HAS_MOVIEPY = True
except ImportError:
    HAS_MOVIEPY = False

try:
    import imageio
    HAS_IMAGEIO = True
except ImportError:
    HAS_IMAGEIO = False


class GifError(Exception):
    """Custom exception for GIF processing errors."""
    pass


@dataclass
class GifConfig:
    """Configuration for GIF generation."""
    default_fps: int = 15
    default_width: int = 480
    default_colors: int = 256
    max_duration: float = 30.0
    default_loop: int = 0  # 0 = infinite


# Presets for common use cases
PRESETS = {
    'twitter': {'width': 512, 'fps': 15, 'max_size_kb': 5000, 'colors': 256},
    'discord': {'width': 256, 'fps': 15, 'max_size_kb': 8000, 'colors': 256},
    'slack': {'width': 480, 'fps': 15, 'max_size_kb': 5000, 'colors': 256},
    'reddit': {'width': 720, 'fps': 20, 'colors': 256},
    'high': {'width': 640, 'fps': 20, 'colors': 256},
    'medium': {'width': 480, 'fps': 15, 'colors': 256},
    'low': {'width': 320, 'fps': 12, 'colors': 128},
    'thumbnail': {'width': 200, 'fps': 10, 'colors': 64, 'max_duration': 3},
    'reaction': {'width': 256, 'fps': 10, 'colors': 64, 'max_duration': 5},
}

# Text position mappings
TEXT_POSITIONS = {
    'top': ('center', 'top'),
    'bottom': ('center', 'bottom'),
    'center': ('center', 'center'),
    'top-left': ('left', 'top'),
    'top-right': ('right', 'top'),
    'bottom-left': ('left', 'bottom'),
    'bottom-right': ('right', 'bottom'),
}


class GifWorkshop:
    """
    Main class for video to GIF conversion.

    Supports chaining operations:
        GifWorkshop("video.mp4").clip(0, 10).resize(480).to_gif("out.gif")
    """

    def __init__(
        self,
        source: Union[str, Path],
        fps: Optional[int] = None,
        width: Optional[int] = None
    ):
        """
        Initialize GIF Workshop.

        Args:
            source: Path to video file
            fps: Target FPS (default: 15)
            width: Target width (default: original)
        """
        if not HAS_MOVIEPY:
            raise ImportError("moviepy is required. Install with: pip install moviepy")

        self.config = GifConfig()
        self._source_path = Path(source)

        if not self._source_path.exists():
            raise FileNotFoundError(f"Video not found: {source}")

        # Load video
        self._clip = VideoFileClip(str(self._source_path))
        self._original_duration = self._clip.duration
        self._original_size = self._clip.size

        # Settings
        self._fps = fps or self.config.default_fps
        self._width = width
        self._colors = self.config.default_colors
        self._loop = self.config.default_loop
        self._max_size_kb: Optional[int] = None
        self._text_overlays: List[Dict] = []
        self._operations: List[str] = []

    def __del__(self):
        """Clean up video clip."""
        if hasattr(self, '_clip') and self._clip:
            self._clip.close()

    def get_info(self) -> Dict[str, Any]:
        """Get video information."""
        return {
            'source': str(self._source_path),
            'duration': self._clip.duration,
            'width': self._clip.size[0],
            'height': self._clip.size[1],
            'fps': self._clip.fps,
            'frame_count': int(self._clip.duration * self._clip.fps),
        }

    def clip(
        self,
        start: Optional[Union[float, str]] = None,
        end: Optional[Union[float, str]] = None
    ) -> 'GifWorkshop':
        """
        Select time range from video.

        Args:
            start: Start time (seconds or "MM:SS" format)
            end: End time (seconds or "MM:SS" format)
        """
        start_sec = self._parse_time(start) if start is not None else 0
        end_sec = self._parse_time(end) if end is not None else self._clip.duration

        # Validate
        if start_sec < 0:
            start_sec = 0
        if end_sec > self._clip.duration:
            end_sec = self._clip.duration
        if start_sec >= end_sec:
            raise GifError(f"Invalid time range: {start_sec} to {end_sec}")

        self._clip = self._clip.subclip(start_sec, end_sec)
        self._operations.append(f"clip({start_sec:.1f}s-{end_sec:.1f}s)")
        return self

    def clip_multi(self, ranges: List[Tuple[float, float]]) -> 'GifWorkshop':
        """Clip and concatenate multiple time ranges."""
        clips = []
        for start, end in ranges:
            clip = self._clip.subclip(start, end)
            clips.append(clip)

        self._clip = concatenate_videoclips(clips)
        self._operations.append(f"clip_multi({len(ranges)} clips)")
        return self

    def _parse_time(self, time_val: Union[float, str]) -> float:
        """Parse time value to seconds."""
        if isinstance(time_val, (int, float)):
            return float(time_val)

        # Parse MM:SS or HH:MM:SS format
        parts = str(time_val).split(':')
        if len(parts) == 2:
            return float(parts[0]) * 60 + float(parts[1])
        elif len(parts) == 3:
            return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
        else:
            return float(time_val)

    def speed(self, factor: float) -> 'GifWorkshop':
        """
        Adjust playback speed.

        Args:
            factor: Speed multiplier (2.0 = 2x faster, 0.5 = half speed)
        """
        if factor <= 0:
            raise GifError("Speed factor must be positive")

        self._clip = self._clip.fx(vfx.speedx, factor)
        self._operations.append(f"speed({factor}x)")
        return self

    def reverse(self) -> 'GifWorkshop':
        """Reverse the clip."""
        self._clip = self._clip.fx(vfx.time_mirror)
        self._operations.append("reverse()")
        return self

    def boomerang(self) -> 'GifWorkshop':
        """Create boomerang effect (forward then reverse)."""
        reversed_clip = self._clip.fx(vfx.time_mirror)
        self._clip = concatenate_videoclips([self._clip, reversed_clip])
        self._operations.append("boomerang()")
        return self

    def resize(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None
    ) -> 'GifWorkshop':
        """
        Resize the video.

        Args:
            width: Target width (maintains aspect if height not specified)
            height: Target height (maintains aspect if width not specified)
        """
        if width and height:
            self._clip = self._clip.resize((width, height))
        elif width:
            self._clip = self._clip.resize(width=width)
            self._width = width
        elif height:
            self._clip = self._clip.resize(height=height)

        self._operations.append(f"resize({width}x{height})")
        return self

    def crop(
        self,
        x: int = 0,
        y: int = 0,
        width: Optional[int] = None,
        height: Optional[int] = None
    ) -> 'GifWorkshop':
        """
        Crop video to region.

        Args:
            x: Left position
            y: Top position
            width: Crop width
            height: Crop height
        """
        w = width or (self._clip.size[0] - x)
        h = height or (self._clip.size[1] - y)

        self._clip = self._clip.crop(x1=x, y1=y, x2=x + w, y2=y + h)
        self._operations.append(f"crop({x},{y},{w},{h})")
        return self

    def crop_to_aspect(self, aspect_w: int, aspect_h: int) -> 'GifWorkshop':
        """
        Crop to specific aspect ratio.

        Args:
            aspect_w: Width ratio (e.g., 16 for 16:9)
            aspect_h: Height ratio (e.g., 9 for 16:9)
        """
        current_w, current_h = self._clip.size
        current_aspect = current_w / current_h
        target_aspect = aspect_w / aspect_h

        if current_aspect > target_aspect:
            # Too wide, crop sides
            new_w = int(current_h * target_aspect)
            x = (current_w - new_w) // 2
            self._clip = self._clip.crop(x1=x, x2=x + new_w)
        else:
            # Too tall, crop top/bottom
            new_h = int(current_w / target_aspect)
            y = (current_h - new_h) // 2
            self._clip = self._clip.crop(y1=y, y2=y + new_h)

        self._operations.append(f"crop_to_aspect({aspect_w}:{aspect_h})")
        return self

    def set_fps(self, fps: int) -> 'GifWorkshop':
        """Set output FPS."""
        self._fps = fps
        self._operations.append(f"set_fps({fps})")
        return self

    def add_text(
        self,
        text: str,
        position: str = 'bottom',
        fontsize: int = 24,
        color: str = 'white',
        font: str = 'Arial',
        stroke_color: Optional[str] = 'black',
        stroke_width: int = 1,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None,
        bg_color: Optional[str] = None
    ) -> 'GifWorkshop':
        """
        Add text overlay.

        Args:
            text: Text to display
            position: Position on screen
            fontsize: Font size
            color: Text color
            font: Font name
            stroke_color: Outline color (None for no outline)
            stroke_width: Outline width
            start_time: When to start showing (None = start)
            end_time: When to stop showing (None = end)
            bg_color: Background color (None for transparent)
        """
        self._text_overlays.append({
            'text': text,
            'position': position,
            'fontsize': fontsize,
            'color': color,
            'font': font,
            'stroke_color': stroke_color,
            'stroke_width': stroke_width,
            'start_time': start_time or 0,
            'end_time': end_time or self._clip.duration,
            'bg_color': bg_color,
        })
        self._operations.append(f"add_text('{text[:20]}...')")
        return self

    def add_caption_bar(
        self,
        text: str,
        position: str = 'bottom',
        background: str = 'black',
        padding: int = 10,
        fontsize: int = 20,
        color: str = 'white'
    ) -> 'GifWorkshop':
        """Add caption with background bar."""
        return self.add_text(
            text,
            position=position,
            fontsize=fontsize,
            color=color,
            bg_color=background
        )

    def _apply_text_overlays(self) -> None:
        """Apply all text overlays to clip."""
        if not self._text_overlays:
            return

        for overlay in self._text_overlays:
            try:
                txt_clip = TextClip(
                    overlay['text'],
                    fontsize=overlay['fontsize'],
                    color=overlay['color'],
                    font=overlay['font'],
                    stroke_color=overlay['stroke_color'],
                    stroke_width=overlay['stroke_width']
                )

                # Position
                pos = overlay['position']
                if pos in TEXT_POSITIONS:
                    txt_clip = txt_clip.set_position(TEXT_POSITIONS[pos])
                else:
                    txt_clip = txt_clip.set_position(('center', 'bottom'))

                # Timing
                txt_clip = txt_clip.set_start(overlay['start_time'])
                txt_clip = txt_clip.set_duration(overlay['end_time'] - overlay['start_time'])

                self._clip = CompositeVideoClip([self._clip, txt_clip])

            except Exception as e:
                # Text rendering can fail, continue without
                print(f"Warning: Could not add text overlay: {e}")

    def filter(self, filter_name: str) -> 'GifWorkshop':
        """
        Apply color filter.

        Available: grayscale, sepia, invert, mirror
        """
        if filter_name == 'grayscale':
            self._clip = self._clip.fx(vfx.blackwhite)
        elif filter_name == 'invert':
            self._clip = self._clip.fx(vfx.invert_colors)
        elif filter_name == 'mirror':
            self._clip = self._clip.fx(vfx.mirror_x)
        elif filter_name == 'sepia':
            # Apply sepia via color matrix
            def sepia_filter(get_frame, t):
                frame = get_frame(t)
                sepia_matrix = np.array([
                    [0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]
                ])
                sepia_frame = frame @ sepia_matrix.T
                return np.clip(sepia_frame, 0, 255).astype(np.uint8)
            self._clip = self._clip.fl(sepia_filter)

        self._operations.append(f"filter({filter_name})")
        return self

    def adjust(
        self,
        brightness: float = 0,
        contrast: float = 0
    ) -> 'GifWorkshop':
        """
        Adjust brightness and contrast.

        Args:
            brightness: -1.0 to 1.0
            contrast: -1.0 to 1.0
        """
        if brightness:
            factor = 1 + brightness
            self._clip = self._clip.fx(vfx.colorx, factor)

        if contrast:
            self._clip = self._clip.fx(vfx.lum_contrast, contrast=int(contrast * 100))

        self._operations.append(f"adjust(b={brightness}, c={contrast})")
        return self

    def fade_in(self, duration: float = 0.5) -> 'GifWorkshop':
        """Add fade in effect."""
        self._clip = self._clip.fx(vfx.fadein, duration)
        self._operations.append(f"fade_in({duration}s)")
        return self

    def fade_out(self, duration: float = 0.5) -> 'GifWorkshop':
        """Add fade out effect."""
        self._clip = self._clip.fx(vfx.fadeout, duration)
        self._operations.append(f"fade_out({duration}s)")
        return self

    def blur(self, intensity: float = 2) -> 'GifWorkshop':
        """Apply blur effect (requires OpenCV)."""
        try:
            import cv2

            def blur_filter(get_frame, t):
                frame = get_frame(t)
                return cv2.GaussianBlur(frame, (0, 0), intensity)

            self._clip = self._clip.fl(blur_filter)
            self._operations.append(f"blur({intensity})")
        except ImportError:
            print("Warning: OpenCV required for blur effect")

        return self

    def optimize(
        self,
        max_size_kb: Optional[int] = None,
        quality: str = 'medium',
        colors: Optional[int] = None,
        lossy: Optional[int] = None
    ) -> 'GifWorkshop':
        """
        Configure optimization settings.

        Args:
            max_size_kb: Target maximum file size
            quality: Preset quality ('low', 'medium', 'high')
            colors: Color palette size (2-256)
            lossy: Lossy compression level (0-100)
        """
        self._max_size_kb = max_size_kb

        if quality == 'low':
            self._fps = min(self._fps, 10)
            self._colors = 64
        elif quality == 'high':
            self._colors = 256
        else:  # medium
            self._colors = 128

        if colors:
            self._colors = min(256, max(2, colors))

        self._operations.append(f"optimize(max={max_size_kb}kb)")
        return self

    def preset(self, preset_name: str) -> 'GifWorkshop':
        """Apply a named preset."""
        if preset_name not in PRESETS:
            raise GifError(f"Unknown preset: {preset_name}")

        settings = PRESETS[preset_name]

        if 'width' in settings:
            self.resize(width=settings['width'])
        if 'fps' in settings:
            self._fps = settings['fps']
        if 'colors' in settings:
            self._colors = settings['colors']
        if 'max_size_kb' in settings:
            self._max_size_kb = settings['max_size_kb']
        if 'max_duration' in settings and self._clip.duration > settings['max_duration']:
            self.clip(end=settings['max_duration'])

        self._operations.append(f"preset({preset_name})")
        return self

    def apply_filter(self, filter_func: Callable) -> 'GifWorkshop':
        """
        Apply custom filter function to each frame.

        Args:
            filter_func: Function that takes PIL Image and returns PIL Image
        """
        def frame_filter(get_frame, t):
            frame = get_frame(t)
            pil_img = Image.fromarray(frame)
            filtered = filter_func(pil_img)
            return np.array(filtered)

        self._clip = self._clip.fl(frame_filter)
        self._operations.append("apply_filter(custom)")
        return self

    def get_frame_at(self, time: float) -> Image.Image:
        """Get frame at specific time as PIL Image."""
        frame = self._clip.get_frame(time)
        return Image.fromarray(frame)

    def get_best_frame(self) -> Image.Image:
        """Get the best frame (middle of clip) as thumbnail."""
        middle = self._clip.duration / 2
        return self.get_frame_at(middle)

    def export_frames(
        self,
        output_dir: Union[str, Path],
        format: str = 'png',
        every_n: int = 1
    ) -> List[str]:
        """
        Export frames as images.

        Args:
            output_dir: Output directory
            format: Image format ('png', 'jpg')
            every_n: Export every Nth frame
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        exported = []
        fps = self._clip.fps
        total_frames = int(self._clip.duration * fps)

        for i in range(0, total_frames, every_n):
            t = i / fps
            frame = self.get_frame_at(t)
            filepath = output_dir / f"frame_{i:05d}.{format}"
            frame.save(filepath)
            exported.append(str(filepath))

        return exported

    def to_gif(
        self,
        output_path: Union[str, Path],
        optimize: bool = True,
        colors: Optional[int] = None,
        loop: Optional[int] = None
    ) -> str:
        """
        Export as GIF.

        Args:
            output_path: Output file path
            optimize: Enable optimization
            colors: Color palette size
            loop: Loop count (0 = infinite)

        Returns:
            Path to created GIF
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Apply text overlays
        self._apply_text_overlays()

        # Determine colors
        n_colors = colors or self._colors
        loop_count = loop if loop is not None else self._loop

        # Generate GIF
        self._clip.write_gif(
            str(output_path),
            fps=self._fps,
            colors=n_colors,
            opt='nq',  # Neural quantization
            loop=loop_count
        )

        # Check file size and re-optimize if needed
        if self._max_size_kb:
            current_size = output_path.stat().st_size / 1024
            if current_size > self._max_size_kb:
                self._optimize_file_size(output_path)

        return str(output_path)

    def _optimize_file_size(self, filepath: Path) -> None:
        """Try to reduce file size to meet target."""
        if not self._max_size_kb:
            return

        current_size = filepath.stat().st_size / 1024

        # Try reducing colors
        colors = self._colors
        fps = self._fps

        while current_size > self._max_size_kb and (colors > 16 or fps > 5):
            if colors > 16:
                colors = max(16, colors // 2)
            else:
                fps = max(5, fps - 2)

            self._clip.write_gif(
                str(filepath),
                fps=fps,
                colors=colors,
                opt='nq',
                loop=self._loop
            )
            current_size = filepath.stat().st_size / 1024

    def to_video(
        self,
        output_path: Union[str, Path],
        codec: str = 'libx264'
    ) -> str:
        """Export as video file (for comparison)."""
        output_path = Path(output_path)
        self._clip.write_videofile(
            str(output_path),
            codec=codec,
            fps=self._fps
        )
        return str(output_path)

    def __repr__(self) -> str:
        return f"GifWorkshop('{self._source_path.name}', {self._clip.duration:.1f}s, {self._clip.size})"


# ==================== CLI ====================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Video to GIF Workshop')
    parser.add_argument('input', help='Input video file')
    parser.add_argument('-o', '--output', required=True, help='Output GIF path')
    parser.add_argument('--start', type=float, help='Start time (seconds)')
    parser.add_argument('--end', type=float, help='End time (seconds)')
    parser.add_argument('--width', type=int, help='Output width')
    parser.add_argument('--fps', type=int, default=15, help='Frames per second')
    parser.add_argument('--speed', type=float, default=1.0, help='Speed multiplier')
    parser.add_argument('--max-size', type=int, help='Max file size in KB')
    parser.add_argument('--text', help='Text overlay')
    parser.add_argument('--text-position', default='bottom', help='Text position')
    parser.add_argument('--preset', help='Apply preset')
    parser.add_argument('--reverse', action='store_true', help='Reverse clip')
    parser.add_argument('--boomerang', action='store_true', help='Boomerang effect')

    args = parser.parse_args()

    # Create workshop
    workshop = GifWorkshop(args.input, fps=args.fps)

    # Apply options
    if args.start is not None or args.end is not None:
        workshop.clip(start=args.start, end=args.end)

    if args.width:
        workshop.resize(width=args.width)

    if args.speed != 1.0:
        workshop.speed(args.speed)

    if args.reverse:
        workshop.reverse()

    if args.boomerang:
        workshop.boomerang()

    if args.text:
        workshop.add_text(args.text, position=args.text_position)

    if args.preset:
        workshop.preset(args.preset)

    if args.max_size:
        workshop.optimize(max_size_kb=args.max_size)

    # Export
    output = workshop.to_gif(args.output)
    print(f"Created: {output}")

    # Show file size
    size_kb = Path(output).stat().st_size / 1024
    print(f"Size: {size_kb:.1f} KB")
