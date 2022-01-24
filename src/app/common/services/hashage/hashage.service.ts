import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HashageService
{
    // Fonction de hashage (faible)
    run(input: string): string
    {
        let hash = 0;
        for (let i = 0; i < input.length; i++) {
            let ch = input.charCodeAt(i);
            hash = ((hash << 5) - hash) + ch;
            hash = hash & hash;
        }
        return hash.toString();
    }
}
