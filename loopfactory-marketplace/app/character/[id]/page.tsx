"use client";

import { useParams } from "next/navigation";
import { Star, Shield, Zap, ChevronRight } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { CharacterViewer } from "@/components/CharacterViewer";
import { SbtBadge } from "@/components/SbtBadge";
import { getCharacterById, ARCHETYPES } from "@/lib/mockData";

export default function CharacterDetailPage() {
  const params = useParams();
  const id = params.id as string;
  const character = getCharacterById(id);

  if (!character) {
    return (
      <div className="container py-24 text-center">
        <h1 className="text-2xl font-bold">Character not found</h1>
        <p className="text-muted-foreground">
          The character you are looking for does not exist.
        </p>
        <Button className="mt-4" asChild>
          <a href="/browse">Back to Browse</a>
        </Button>
      </div>
    );
  }

  const archetypeInfo = ARCHETYPES[character.archetype];
  const evolutionStages = Array.from(
    { length: Math.max(4, character.evolutionStage) },
    (_, i) => i + 1
  );

  return (
    <div className="container py-8">
      <div className="mb-6">
        <a
          href="/browse"
          className="text-sm text-muted-foreground hover:text-foreground"
        >
          &larr; Back to Browse
        </a>
      </div>

      <div className="grid gap-8 lg:grid-cols-2">
        {/* 3D Viewer */}
        <CharacterViewer
          archetype={character.archetype}
          className="aspect-square"
        />

        {/* Details */}
        <div className="space-y-6">
          <div>
            <div className="mb-2 flex items-center gap-2">
              <Badge variant="secondary">{character.type}</Badge>
              {character.poaiVerified && (
                <Badge
                  variant="outline"
                  className="flex items-center gap-1 border-emerald-500/50 text-emerald-600"
                >
                  <Shield className="h-3 w-3" />
                  POAI Verified
                </Badge>
              )}
            </div>
            <h1 className="text-3xl font-bold tracking-tight">
              {character.name}
            </h1>
            <div className="mt-2 flex items-center gap-4 text-sm text-muted-foreground">
              <span className="flex items-center gap-1">
                <Star className="h-4 w-4 fill-amber-400 text-amber-400" />
                {character.rating} ({character.reviewCount} reviews)
              </span>
              <span>{character.author}</span>
            </div>
          </div>

          <p className="text-muted-foreground">{character.description}</p>

          <SbtBadge
            sbtType={character.sbtType}
            charterRef={character.charterRef}
            riskTier={character.riskTier}
            archetype={character.archetype}
            evolutionStage={character.evolutionStage}
          />

          {/* Archetype Info */}
          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm">Archetype</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="flex items-center gap-3">
                <span
                  className="inline-block h-8 w-8 rounded-lg border shadow-sm"
                  style={{ backgroundColor: archetypeInfo.color }}
                />
                <div>
                  <p className="font-semibold">{character.archetype}</p>
                  <p className="text-xs text-muted-foreground">
                    {archetypeInfo.material}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Evolution Stages */}
          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm">Evolution</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex items-center gap-2">
                {evolutionStages.map((stage, idx) => {
                  const active = stage <= character.evolutionStage;
                  return (
                    <div key={stage} className="flex items-center gap-2">
                      <div
                        className={`flex h-8 w-8 items-center justify-center rounded-full border text-xs font-bold ${
                          active
                            ? "border-transparent text-white"
                            : "border-muted bg-muted text-muted-foreground"
                        }`}
                        style={
                          active
                            ? { backgroundColor: archetypeInfo.color }
                            : undefined
                        }
                      >
                        {stage}
                      </div>
                      {idx < evolutionStages.length - 1 && (
                        <ChevronRight className="h-4 w-4 text-muted-foreground" />
                      )}
                    </div>
                  );
                })}
              </div>
            </CardContent>
          </Card>

          {character.poaiScore && (
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm">POAI Audit Score</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex items-center gap-3">
                  <div className="text-3xl font-bold text-emerald-600">
                    {character.poaiScore}
                  </div>
                  <div className="text-sm text-muted-foreground">/ 100</div>
                </div>
                <div className="mt-2 h-2 w-full overflow-hidden rounded-full bg-muted">
                  <div
                    className="h-full rounded-full bg-emerald-500"
                    style={{ width: `${character.poaiScore}%` }}
                  />
                </div>
              </CardContent>
            </Card>
          )}

          <div className="flex items-center gap-4 pt-4">
            <span className="text-3xl font-bold">${character.price}</span>
            <Button size="lg">
              <Zap className="mr-2 h-4 w-4" />
              Acquire Character
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
