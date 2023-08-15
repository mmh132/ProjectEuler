#include <stdio.h>
#include <time.h>
#include <set>
#include <map>
#include <array>

typedef unsigned int uint;
typedef unsigned long long ull;
typedef unsigned char uchar;

static const uint w = 7; // need w = 7
static const uint h = w;
static const uint wh = w*h;

struct BLOB {
    ull mask;
    uint a;
    uint xmax;
    uint ymax;
    BLOB (ull mask=0, uint a=0, uint x=0, uint y=0)
            : mask(mask), a(a), xmax(x), ymax(y) {}
    bool unreachable (uint x, uint y) const {
        if (y>ymax+1)
            return true;
        else if (y==ymax+1 && x>xmax)
            return true;
        return false;
    }
    bool touches (uint x, uint y) const {
        uint icell = y*w + x;
        if ((1ULL<<icell) & mask)
            return false;
        if (x>0 && ((1ULL<<(icell-1)) & mask))
            return true;
        if (y>0 && ((1ULL<<(icell-w)) & mask))
            return true;
        return false;
    }
};

static uint nblobsmax = 0;

static const uint NSTATE = 24;
typedef std::array<uchar,NSTATE> STATE;
static std::map<STATE,ull> cache;

static ull dfs (uint icell, BLOB *blobs, uint nblobs, uint amax)
{
	nblobsmax = std::max (nblobsmax, nblobs);

	if (icell==wh)
		return amax;

	uint asum = 0;
	for (uint i=0; i<nblobs; i++) {
		const BLOB &blob = blobs[i];
		asum += blob.a;
	}
	if (asum+wh-icell<=amax)
		return amax << (wh-icell);

	STATE state;
	uint nstate = 0;
	state[nstate++] = icell;
	state[nstate++] = amax;
	for (uint i=0; i<nblobs; i++) {
		const BLOB &blob = blobs[i];
		state[nstate++] = 100+blob.a;
		uint ymax = std::min (blob.ymax+1, h-1);
		for (uint y=blob.ymax; y<=ymax; y++) {
			for (uint x=0; x<w; x++) {
				if (blob.touches (x, y)) {
					uint icell2 = y*w + x;
					state[nstate++] = icell2;
				}
			}
		}
	}
	static uint nstatemax = 0;
	if (nstate>nstatemax) {
		nstatemax = nstate;
		printf (">>> nstatemax = %d\n", nstatemax);
	}
	if (nstate>NSTATE) {
		printf ("ERROR: NSTATE too small\n");
		throw;
	}
	while (nstate<NSTATE)
		state[nstate++] = 0;
	if (cache.count (state))
		return cache[state];

	uint x = icell%w;
	uint y = icell/w;

	BLOB blobs2[w];
	uint nblobs2 = 0;
	for (uint i=0; i<nblobs; i++) {
		const BLOB &blob = blobs[i];
		if (blob.unreachable (x, y)) {
			;
		} else {
			blobs2[nblobs2] = blob;
			nblobs2++;
		}
	}
	ull sumwhite = dfs (icell+1, blobs2, nblobs2, amax);

	nblobs2 = 0;
	uint amax2 = amax;
	ull newmask = 1ULL << icell;
	uint newa = 1;
	for (uint i=0; i<nblobs; i++) {
		const BLOB &blob = blobs[i];
		if (blob.unreachable (x, y)) {
			;
		} else if (blob.touches (x, y)) {
			newmask |= blob.mask;
			newa += blob.a;
		} else {
			blobs2[nblobs2] = blob;
			nblobs2++;
		}
	}
	blobs2[nblobs2] = BLOB (newmask, newa, x, y);
	nblobs2++;
	amax2 = std::max (amax2, newa);
	ull sumblack = dfs (icell+1, blobs2, nblobs2, amax2);

	ull ret = sumwhite + sumblack;
	cache[state] = ret;
	const uint delta = 100000;
	if (cache.size ()%delta==0)
		printf ("cache.size = %d\n", cache.size ());
	
	return ret;
}

int main ()
{
    // Dfs:
    uint start = time (NULL);
    ull sum1 = dfs (0, NULL, 0, 0);
    ull sum2 = 1ULL<<wh;
    printf ("ev = %.8f (%lld/%lld)\n", (double)sum1/sum2, sum1, sum2);
    printf ("nblobsmax = %d\n", nblobsmax); // w=6-->nbmax=4
    printf ("cache.size = %d\n", cache.size ());
    printf ("%d sec\n", time(NULL)-start);
    return 0;
/*
    w=6:
    ev = 10.74254251 (738221900249/68719476736)
    nblobsmax = 4
    cache.size = 2409590
    36 sec
*/
}