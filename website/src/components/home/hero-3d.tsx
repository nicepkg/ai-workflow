"use client";

import {
  Sphere,
  MeshDistortMaterial,
  Float,
  Stars,
  PerspectiveCamera,
} from "@react-three/drei";
import { Canvas, useFrame } from "@react-three/fiber";
import { useRef } from "react";
import type * as THREE from "three";

function AnimatedSphere() {
  const sphereRef = useRef<THREE.Mesh>(null);

  useFrame((state) => {
    const t = state.clock.getElapsedTime();
    if (sphereRef.current) {
      sphereRef.current.rotation.z = t * 0.1;
      sphereRef.current.rotation.x = t * 0.15;
    }
  });

  return (
    <Sphere visible args={[1, 64, 64]} scale={2.0} ref={sphereRef}>
      <MeshDistortMaterial
        color="#a78bfa" // Lighter purple (Purple-400)
        attach="material"
        distort={0.4}
        speed={2}
        roughness={0.4} // Increased roughness to show color better
        metalness={0.2} // Decreased metalness so it doesn't reflect the black void
        emissive="#8b5cf6" // Purple-500 glow
        emissiveIntensity={0.8} // Strong glow
        wireframe={true}
      />
    </Sphere>
  );
}

export function Hero3D() {
  return (
    <div className="pointer-events-none absolute inset-0 -z-10 h-full w-full opacity-40 dark:opacity-80">
      <Canvas>
        <PerspectiveCamera makeDefault position={[0, 0, 6]} />
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={1.5} />
        <pointLight position={[-10, -10, -10]} color="#3b82f6" intensity={1} />

        <Stars
          radius={100}
          depth={50}
          count={3000}
          factor={4}
          saturation={0}
          fade
          speed={1}
        />

        <Float speed={2} rotationIntensity={1} floatIntensity={1}>
          <AnimatedSphere />
          {/* <InnerCore /> */}
        </Float>
      </Canvas>
    </div>
  );
}
