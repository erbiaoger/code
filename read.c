#include <stdio.h>


int main()
{

  int nx = 2250;
  int nz = 750;
  float a[nz][nx];

  FILE *fpdat = fopen("1.dat", "rb");
  for (int ix = 0; ix < nx; ix++)
  {
    for (int iz = 0; iz < nz; iz++)
    {
    fread(a, sizeof(float), 1, fpdat);
    }

  }
  for (int j = 0; j < nz; j++)
  {
    for (int i = 0; i < nx; i++)
    {
      printf("%f", a[i][j]);
    }
  }
  fclose(fpdat);


  return 0;
}
