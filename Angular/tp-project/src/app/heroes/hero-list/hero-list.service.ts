import { Injectable } from '@angular/core';
import {Hero} from "../hero/hero.model";
import {concatMap, delay, from, Observable, of} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class HeroListService {

  mockHeroesList: Array<Hero> = [
    new Hero(1, 'Batman', 10),
    new Hero(2, 'Pacman', 20),
    new Hero(3, 'Superman', 30),
  ]
  constructor() { }

  getAllHeroes(): Observable<Array<Hero>>{
    return of(this.mockHeroesList).pipe(delay(1000));
  }

  rotateAllHeroes(): Observable<Hero> {
    return from(this.mockHeroesList).pipe(concatMap(item => of(item).pipe(delay(1000))));}

}
